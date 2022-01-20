# Question 2 

### Need to connect to sql server database , "Data Source=localhost\SQLEXPRESS; Integrated Security= true" is my default connection string

### Run the function Assignment.cs and it will ask for the location path of FILES folder which contains csv files, it will ask untill coreccttly specified , and the example path will be provided in case of failure

### The programm will then create database with tables , parse the csv files and insert into database with sql bulk copy method

### The files with errors will be moved to error folder , otherwise to processed folder. Both folders are at the same location as files folder

### End results in database , 1000 rows total

<img src="/question2/result.jpeg" width="1000"/>
