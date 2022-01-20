

def view(conn):
    cursor = conn.cursor()
    print("Printing rows for the query B ")
    cursor.execute('''   
    SELECT TOP 10 d.amount_eur, c.email,c.brand_name, d.calendar_date
    FROM [question1].[dbo].[DepositTransaction] d
    LEFT JOIN [question1].[dbo].[Customer] c 
    ON c.customer_id = d.customer_id
    ORDER BY d.amount_eur DESC
     ''')
    for row in cursor.fetchall():
        print(row)

    print("\n \n Printing rows for the query C")
    cursor.execute('''   
    SELECT  c.brand_name, COUNT(*) as total_number , SUM(d.amount_eur) as amount
    FROM [question1].[dbo].[DepositTransaction] d
    LEFT JOIN [question1].[dbo].[Customer] c 
    ON c.customer_id = d.customer_id
    LEFT JOIN [question1].[dbo].[PaymentStatus] p 
    ON p.payment_status_id = d.payment_status_id
    GROUP BY p.name,c.brand_name
    HAVING p.name='Failed'
     ''')
    for row in cursor.fetchall():
        print(row)

    print("\n \n Printing rows for the query D")
    cursor.execute('''   
    SELECT  c.brand_name,p.product_name, SUM(g.turnover) as turnover , SUM(g.total_acc_revenue) as accounting_revenue
    FROM [question1].[dbo].[GamePlayTransaction] g
    LEFT JOIN [question1].[dbo].[Customer] c
    ON c.customer_id = g.customer_id
    LEFT JOIN [question1].[dbo].[ProviderProduct] p
    ON p.provider_product_id = g.provider_product_id
    GROUP BY g.calendar_date, p.product_name, c.brand_name
    HAVING g.calendar_date BETWEEN '20210101' AND '20210106'
     ''')
    for row in cursor.fetchall():
        print(row)

    print("\n \n Printing rows for the query E")
    cursor.execute('''   
    SELECT  p.product_name, AVG(g.game_win) as average_gamewin 
    FROM [question1].[dbo].[GamePlayTransaction] g
    LEFT JOIN [question1].[dbo].[ProviderProduct] p
    ON p.provider_product_id = g.provider_product_id
    GROUP BY p.product_name
     ''')
    for row in cursor.fetchall():
        print(row)


    print("\n \n Printing rows for the query F")
    cursor.execute('''   
    SELECT  c.customer_id, c.email, SUM(g.turnover) as total_turnover 
    FROM [question1].[dbo].[GamePlayTransaction] g
    LEFT JOIN [question1].[dbo].[Customer] c
    ON c.customer_id = g.customer_id
    GROUP BY c.customer_id,c.email
    HAVING SUM(g.turnover)>500
     ''')
    for row in cursor.fetchall():
        print(row)
