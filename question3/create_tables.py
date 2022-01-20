

def create_dim(conn):
    cursor = conn.cursor()
    print("Creating Customer Dimension")
    cursor.execute('''
            CREATE TABLE [AdventureWorks2019].[dbo].[CustomerDim] (
                        customer_key INTEGER IDENTITY(1,1) PRIMARY KEY,
                        CustomerID INTEGER NOT NULL,
                        AccountNumber VARCHAR(max)  NULL,
                        customer_modified_date DATETIME NULL,
                        Demographics XML NULL,
                        EmailPromotion INTEGER NULL,
                        FirstName VARCHAR(max) NULL,
                        LastName VARCHAR(max) NULL,
                        MiddleName VARCHAR(max) NULL,
                        NameStyle BIT NULL,
                        PersonType VARCHAR(max) NULL,
                        Suffix VARCHAR(max) NULL,
                        Title VARCHAR(max) NULL,
                        person_modified_date DATETIME NULL,
                        business_entity_modified_date DATETIME NULL,
                        EmailAddress VARCHAR(max) NULL,
                        email_modified_date DATETIME NULL,
                        PhoneNumber VARCHAR(max) NULL,
                        phone_modified_date DATETIME NULL,
                        AddressLine1 VARCHAR(max) NULL, 
                        AddressLine2 VARCHAR(max) NULL,
                        City VARCHAR(max) NULL,
                        SpatialLocation GEOGRAPHY NULL,
                        address_modified_date DATETIME NULL,
                        store_data VARCHAR(max) NULL,
                        territory_data  VARCHAR(max) NULL)
     ''')
    conn.commit()

def create_fact(conn):
    cursor = conn.cursor()
    print("Creating SalesOrder Fact")
    cursor.execute('''
                CREATE TABLE [AdventureWorks2019].[dbo].[FactSalesOrder](
                SalesOrderKey INTEGER NULL,
                SalesOrderStatusKey INTEGER NULL,
                SalesOnlineOrderFlag INTEGER NULL,
                SalesOrderAccountNumber INTEGER NULL,
                SalesOrderCustomerKey INTEGER NULL,
                SalesPersonKey INTEGER NULL,
                TerritoryKey INTEGER NULL,
                BillToAddressKey INTEGER NULL,
                ShipToAddressKey INTEGER NULL,
                ShipMethodKey INTEGER NULL,
                ProductKey INTEGER NULL,
                SpecialOfferKey INTEGER NULL,
                SalesOrderDetailKey INTEGER NULL,
                SubTotal MONEY NULL,
                TaxAmt MONEY NULL,
                Freight MONEY NULL,
                TotalDue MONEY NULL,
                OrderQty MONEY NULL,
                UnitPrice MONEY NULL,
                UnitPriceDiscount MONEY NULL,
                LineTotal REAL NULL,
                SalesOrderDetailModifiedDateKey INTEGER NULL,
                SalesOrderDateKey INTEGER NULL,
                SalesOrderDueDateKey INTEGER NULL,
                SalesOrderShipDateKey INTEGER NULL,
                SalesOrderModifiedDateKey INTEGER NULL)
                
                CREATE nonclustered index NISalesOrderCustomerKey ON [AdventureWorks2019].[dbo].[FactSalesOrder] (SalesOrderCustomerKey);
     ''')
    conn.commit()
