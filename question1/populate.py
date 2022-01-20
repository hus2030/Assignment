
# Populates first the leaf entities then Customer which references country and transaction tables at the end

def populate_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO [question1].[dbo].[Country] (country_name)
    SELECT distinct customer_country
      FROM  (select customer_country from [question1].[dbo].[StagingGame]
             union all 
             select customer_country from [question1].[dbo].[StagingDeposit]) d
              
    
    INSERT INTO [question1].[dbo].[PaymentMethod] (name,type)
    SELECT distinct payment_method_name, payment_method_type
      FROM [question1].[dbo].[StagingDeposit]
    
    
    INSERT INTO [question1].[dbo].[PaymentStatus] (name,description)
    SELECT distinct payment_status_name, payment_status_description
      FROM [question1].[dbo].[StagingDeposit]
    
    
    
    INSERT INTO [question1].[dbo].[ProviderProduct] (product_name,provider_name)
    SELECT distinct provider_product_name, provider_name
      FROM [question1].[dbo].[StagingGame]
     ''')
    conn.commit()


    cursor.execute('''
    INSERT INTO [question1].[dbo].[Customer] (country_id,email,brand_name,account_status)
    SELECT distinct (select country_id from [question1].[dbo].[Country] where d.customer_country=country_name),
                            customer_email,customer_brand_name,customer_account_status
      FROM  (select customer_country,customer_email,customer_brand_name,customer_account_status from [question1].[dbo].[StagingGame]
             union all 
             select customer_country,customer_email,customer_brand_name,customer_account_status from [question1].[dbo].[StagingDeposit]) d
    
    
     ''')
    conn.commit()


    cursor.execute('''
    
    INSERT INTO [question1].[dbo].[DepositTransaction] (customer_id, payment_method_id, payment_status_id, amount_eur, calendar_date)
    SELECT  (select customer_id from [question1].[dbo].[Customer] where d.customer_email = email),
            (select payment_method_id from [question1].[dbo].[PaymentMethod] where d.payment_method_name = name),
            (select payment_status_id from [question1].[dbo].[PaymentStatus] where d.payment_status_name = name and d.payment_status_description = description),
            amount_eur, calendar_date
      FROM [question1].[dbo].[StagingDeposit] d
    
    
    
    INSERT INTO [question1].[dbo].[GamePlayTransaction] (customer_id, provider_product_id, device_name, rounds, turnover, game_win, bonus_cost, total_acc_revenue, calendar_date)
    SELECT  (select customer_id from [question1].[dbo].[Customer] where g.customer_email = email),
            (select provider_product_id from [question1].[dbo].[ProviderProduct] where g.provider_name=provider_name and g.provider_product_name=product_name),
            device_name, rounds, turnover, game_win, bonus_cost, total_acc_revenue, calendar_date
      FROM [question1].[dbo].[StagingGame] g
     ''')
    conn.commit()