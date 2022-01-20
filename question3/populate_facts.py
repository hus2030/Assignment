

def populate_facts(conn):
    cursor = conn.cursor()
    print("Population SalesOrderFact")
    cursor.execute('''
                    INSERT INTO [AdventureWorks2019].[dbo].[FactSalesOrder]
                    SELECT
                    NULL AS SalesOrderKey,
                    NULL SalesOrderStatusKey,
                    NULL AS SalesOnlineOrderFlag,
                    NULL AS SalesOrderAccountNumber,
                    c.customer_key AS SalesOrderCustomerKey,
                    NULL AS SalesPersonKey,
                    NULL AS TerritoryKey,
                    NULL AS BillToAddressKey,
                    NULL AS ShipToAddressKey,
                    NULL AS ShipMethodKey,
                    NULL AS ProductKey,
                    NULL AS SpecialOfferKey,
                    NULL AS SalesOrderDetailKey,
                    h.SubTotal,
                    h.TaxAmt,
                    h.Freight,
                    h.TotalDue,
                    d.OrderQty,
                    d.UnitPrice,
                    d.UnitPriceDiscount,
                    d.LineTotal,
                    CONVERT(INTEGER, CONVERT(VARCHAR(8),d.ModifiedDate,112)) AS SalesOrderDetailModifiedDateKey,
                    CONVERT(INTEGER, CONVERT(VARCHAR(8),h.OrderDate,112)) AS SalesOrderDateKey,
                    CONVERT(INTEGER, CONVERT(VARCHAR(8),h.DueDate,112)) AS SalesOrderDueDateKey,
                    CONVERT(INTEGER, CONVERT(VARCHAR(8),h.ShipDate,112)) AS SalesOrderShipDateKey,
                    CONVERT(INTEGER, CONVERT(VARCHAR(8),h.ModifiedDate,112)) AS SalesOrderModifiedDateKey
                    FROM [AdventureWorks2019].[Sales].[SalesOrderDetail] d
                    LEFT JOIN [AdventureWorks2019].[Sales].[SalesOrderHeader] h ON d.SalesOrderID = h.SalesOrderID
                    LEFT JOIN [AdventureWorks2019].[dbo].[CustomerDim] c ON c.CustomerID = h.CustomerID
     ''')
    conn.commit()
