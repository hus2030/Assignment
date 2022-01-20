# Question 1

### pip install requirments.txt 
### Update  connection.ini file with server name and the path of csv files for DepositTransaction(Question1a.csv) and GamePlayTransaction(Question1b.csv)
### then python main.py to run the application 
### it will output the query results in the console . The results are provided here too

### Prequisite notes :
1) I seperated the csv sheets to different files and uploaded them here 
2) the path to the csv files should be specified in the configuration ini file
3) the server name for the database connection screen should also be specified in ini file

### Steps :
1) creation of all neccesary tables (staging tables and main tables from the data model)
2) filling the staging tables with the data from csv files
3) populating the main tables with the data from staging tables 
   - first the leaf tables are populated , not to cause reference errors
4) then the output of the required queries is printed 


### Data Model

<img src="/question1/files/DataModel.jpg" width="1000"/>

### Results
1)
