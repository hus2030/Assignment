# Question 3

### This part assumes that you already have AdventureWorksDatabase recovered in sql server
### -pip install requirments.txt 
### -update  connection.ini file with sql server name 
### -then python main.py to run the application 
### Then check the dbo.CustomerDim and dbo.FactSalesOrder tables for data


## Steps :
1) creation of customer dimension table and saleorder fact table
2) populating customer dimension using important attributes from Sales.Customer, Person.Person, Person.EmailAddress, Person.PersonPhone, Person.BussinessEntityID, Person.Address
3) populating fact table using surrogate key from customer dimension


## Choice of attributes for SalesOrder fact
### - RED - keys i considered important , all of them will be NULL except Customer Key 
### - GREEN - measures I considered important
### - Yelloq - dates , I converted them to integer with 112 style to keep them in fact table

<img src="/question3/faceSaleOrder.jpg" width="1000"/>


## Notes :
1) Ideally there shouldnt be NULL keys in fact table , but as i dont have that dimensions yet I kept them as NUlL , except Customer Key
