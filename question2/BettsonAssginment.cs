using Microsoft.VisualBasic.FileIO;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Question2
{
    class Program
    {
        private static DataTable GetDataFromCsv(string csv_file_path)
        {
            DataTable csvData = new DataTable();
            try
            {   // Parsing csl file to data table
                using (TextFieldParser csvReader = new TextFieldParser(csv_file_path))
                {
                    csvReader.SetDelimiters(new string[] { "," });
                    csvReader.HasFieldsEnclosedInQuotes = true;
                    string[] cols = csvReader.ReadFields();
                    foreach (string column in cols)
                    {
                        DataColumn datecolumn = new DataColumn(column);
                        datecolumn.AllowDBNull = true;
                        csvData.Columns.Add(datecolumn);
                    }
                    while (!csvReader.EndOfData)
                    {
                        string[] fieldData = csvReader.ReadFields();
                        //Making empty value as null
                        for (int i = 0; i < fieldData.Length; i++)
                        {
                            if (fieldData[i] == "")
                            {
                                fieldData[i] = null;
                            }
                        }
                        csvData.Rows.Add(fieldData);
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
                return null;
            }
            Console.WriteLine(csvData);
            return csvData;
        }


        //Inserting data extractred from csv tables to the created tables , for that we create the column mappings between datatable and table , i made them identical so it is easy to create mappings
        static void InsertData(DataTable csvData, SqlConnection conn )
        {

            using (SqlBulkCopy s = new SqlBulkCopy(conn))
                {
                    s.DestinationTableName = "Question2.dbo.Sale";
                foreach (var column in csvData.Columns)
                {
                    s.ColumnMappings.Add(column.ToString(), column.ToString());
                    
                }
                    s.WriteToServer(csvData);
                }
                
        }


        static void CreateDatabaseAndTable(SqlConnection conn)
        {

            String comm;
            String comm2;
            comm = "CREATE DATABASE [Question2];";

            comm2 = @"
                    CREATE TABLE [Question2].[dbo].[Sale](
	                    [Region] [nvarchar](50) NULL,
	                    [Country] [nvarchar](50) NULL,
	                    [Item Type] [nvarchar](50) NULL,
	                    [Sales Channel] [nvarchar](50) NULL,
	                    [Order Priority] [nvarchar](50) NULL,
	                    [Order Date] [date] NULL,
	                    [Order ID] [nvarchar](50) NULL,
	                    [Ship Date] [date] NULL,
	                    [Units Sold] [int] NULL,
	                    [Unit Price] [real] NULL,
	                    [Unit Cost] [real] NULL,
	                    [Total Revenue] [real] NULL,
	                    [Total Cost] [real] NULL,
	                    [Total Profit] [real] NULL
                    ) ";

            using (SqlCommand Comm = new SqlCommand(comm, conn))
            using (SqlCommand Comm2 = new SqlCommand(comm2, conn))
            {

                // Creating database Question2

                try
                {

                    Comm.ExecuteNonQuery();
                    Console.WriteLine("Database created succesfully");
                }
                catch (System.Exception ex)
                {
                    Console.WriteLine(ex.ToString());
                }

                // Creating table Sale
                try
                {

                    Comm2.ExecuteNonQuery();
                    Console.WriteLine("Table created succesfully");
                }
                catch (System.Exception ex)
                {
                    Console.WriteLine(ex.ToString());
                }

            }

        }








        static void Main(string[] args)
        {
            using (SqlConnection conn = new SqlConnection(@"Data Source=localhost\SQLEXPRESS; Integrated Security= true"))
            {

                // DEFAULT C:\Users\huseyn98\Desktop\FILES\       Getting the location of files folder from the console argument provided by user
                // The loop will continue untill the provided location is correct
                string[] dirs= null;
                var state = 0;
                while (state < 2)
                {
                    try
                    {
                        System.Console.WriteLine("Please enter location of your FILES folder which contains csv files.");
                        string line = Console.ReadLine();
                        dirs = Directory.GetFiles(@line, "*.csv");
                        if (state == 0)
                        {
                            state = 2;
                        }
                    }
                    catch
                    {
                        System.Console.WriteLine(@"Incorrect location , example : C:\Users\huseyn98\Desktop\FILES\ ");
                    }
                }


                // Creating database and tables
                conn.Open();
                CreateDatabaseAndTable(conn);


                foreach (string dir in dirs)
                {
                    Console.WriteLine(dir);

                    // EXtracting data from csv files
                    DataTable d = GetDataFromCsv(dir);

                    // If error or datatable is empty copy the csv file to error folder
                    if ((d is null) || (d.Rows.Count==0) )
                    {
                        string source = @dir;
                        string destination = source.Replace("FILES", "ERROR");
                        Console.WriteLine("Moving file to error folder ");
                        System.IO.File.Copy(source, destination,true);
                    }
                    // else copy csv file to processed folder
                    else
                    {
                        // Inserting data into the created table
                        InsertData(d, conn);

                        string source = @dir;
                        string destination = source.Replace("FILES", "PROCCESSED");
                        Console.WriteLine("Moving file to processed folder ");
                        System.IO.File.Copy(source, destination,true);
                        // Inserting data into the created table
                        InsertData(d, conn);
                    }

                }
                conn.Close();
            }
            Console.WriteLine("Complete, check the table dbo.Sale ");
            Console.ReadLine();

        }
    }
}
