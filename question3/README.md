# Question 3

### - this part assumes that you already have AdventureWorksDatabase recovered in sql server
### - pip install -r requirments.txt 
### - update  connection.ini file with sql server name 
### - then python main.py to run the application 
### - then check the dbo.CustomerDim and dbo.FactSalesOrder tables for data


## Steps :
1) creation of customer dimension table and saleorder fact table
2) populating customer dimension using important attributes from Sales.Customer, Person.Person, Person.EmailAddress, Person.PersonPhone, Person.BussinessEntityID, Person.Address
3) populating fact table using surrogate key from customer dimension


## Choice of attributes for SalesOrder fact
### - RED - keys i considered important , all of them will be NULL except Customer Key 
### - GREEN - measures I considered important
### - Yellow - dates , I converted them to integer with 112 style to keep them in fact table


<img src="/question3/photos/faceSaleOrder.jpg" width="1000"/>


## Notes :
1) Ideally there shouldnt be NULL keys in fact table , but as i dont have that dimensions yet I kept them as NUlL , except Customer Key
2) I left joined salesorder header to salesorder detail to get more data in fact


## Snapshots from database (not everything fits to screenshot)

### Customer Dimension 

<img src="/question3/photos/DimSnap.jpeg" width="1000"/>


### SalesOrder Fact 

<img src="/question3/photos/FactSnap.jpeg" width="1000"/>
