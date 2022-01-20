
import pandas as pd

def staging_fill(conn , deposit_link, gameplay_link):
    cursor = conn.cursor()
    dfDeposit = pd.read_csv (deposit_link)
    dfGame = pd.read_csv (gameplay_link)
    # Filling DepositTransaction staging table from the csv values
    for index,row in dfDeposit.iterrows():
        # print([type(x) for x in row])
        cursor.execute('''
        INSERT INTO [question1].[dbo].[StagingDeposit]([calendar_date]
                       ,[customer_email]
                       ,[customer_brand_name]
                       ,[customer_country]
                       ,[customer_account_status]
                       ,[payment_method_name]
                       ,[payment_method_type]
                       ,[payment_status_name]
                       ,[payment_status_description]
                       ,[amount_eur]) VALUES(?,?,?,?,?,?,?,?,?,?)
                       ''',
                       str(row['CalendarDate']),row['CustomerEmail'],row['CustomerBrandName'],row['CustomerCountry'],
                       row['CustomerAccountStatus'],row['PaymentMethodName'],row['PaymentMethodType'],row['PaymentStatusName'],
                       row['PaymentStatusDescription'], row['amount_eur'] )
        conn.commit()
    #Filling GameplayTransaction staging table from the csv values
    dfGame = dfGame.where(dfGame.notnull(), None)
    dfGame['bonus cost'] = dfGame['bonus cost'].fillna(0)
    for index,row in dfGame.iterrows():
        cursor.execute('''
        INSERT INTO [question1].[dbo].[StagingGame](
                        [calendar_date]
                       ,[customer_email]
                       ,[customer_brand_name]
                       ,[customer_country]
                       ,[customer_account_status]
                       ,[provider_name]
                       ,[provider_product_name]
                       ,[device_name]
                       ,[rounds]
                       ,[turnover]
                       ,[game_win]
                       ,[bonus_cost]
                       ,[total_acc_revenue]
                       ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                       ''',
                       str(row['CalendarDate']),row['CustomerEmail'],row['CustomerBrand'],row['CustomerCountry'],
                       row['CustomerStatus'],row['ProviderName'],row['ProviderProductName'],row['DeviceName'],
                       row['rounds'], row['turnover_EUR'] ,row['gameWin_EUR'], row['bonus cost'],row['totalAccountingRevenue_EUR'])
        conn.commit()