

def populate_dims(conn):
    cursor = conn.cursor()
    print("Population Customer Dimension")
    cursor.execute('''
                INSERT INTO [AdventureWorks2019].[dbo].[CustomerDim]
                SELECT 
                    c.CustomerID,
                    c.AccountNumber,
                    c.ModifiedDate as customer_modified_date,
                    p.Demographics,
                    p.EmailPromotion,
                    p.FirstName,
                    p.LastName,
                    p.MiddleName,
                    p.NameStyle,
                    p.PersonType,
                    p.Suffix,
                    p.Title,
                    p.ModifiedDate as person_modified_date,
                    b.ModifiedDate as business_entity_modified_date,
                    e.EmailAddress,
                    e.ModifiedDate as email_modified_date,
                    ph.PhoneNumber,
                    ph.ModifiedDate as phone_modified_date,
                    a.AddressLine1, a.AddressLine2,
                    a.City,
                    a.SpatialLocation,
                    a.ModifiedDate as address_modified_date,
                    NULL as store_data,
                    NULL as territory_data
                FROM [AdventureWorks2019].[Sales].[Customer] c
                LEFT JOIN [AdventureWorks2019].[Person].[Person] p ON c.PersonID = p.BusinessEntityID
                LEFT JOIN [AdventureWorks2019].[Person].[EmailAddress] e ON e.BusinessEntityID = p.BusinessEntityID
                LEFT JOIN [AdventureWorks2019].[Person].[PersonPhone] ph ON ph.BusinessEntityID = p.BusinessEntityID
                LEFT JOIN [AdventureWorks2019].[Person].[BusinessEntityAddress] b ON b.BusinessEntityID = p.BusinessEntityID
                LEFT JOIN [AdventureWorks2019].[Person].[Address] a ON a.AddressID = b.AddressID
     ''')
    conn.commit()
