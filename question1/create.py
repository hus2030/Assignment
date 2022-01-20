
def create_database(conn):
    cursor = conn.cursor()
    #Creating the database
    cursor.execute('''
     CREATE DATABASE [question1];
     ''')
    conn.commit()

def create_tables(conn):
    cursor = conn.cursor()
    # Creating the tables
    cursor.execute('''
     CREATE TABLE question1.dbo.StagingGame (
            game_id INTEGER IDENTITY(1,1) PRIMARY KEY,
            calendar_date varchar(max)  NULL,
            customer_email varchar(max)  NULL,
            customer_brand_name varchar(max)  NULL,
            customer_country varchar(max)  NULL,
            customer_account_status varchar(max)  NULL,
            provider_name varchar(max)  NULL,
            provider_product_name varchar(max)  NULL,
            device_name varchar(max)  NULL,
            rounds INT  NULL,
            turnover REAL NULL,
            game_win REAL NULL,
            bonus_cost REAL NULL,
            total_acc_revenue REAL NULL)
    
    
    
    
     CREATE TABLE question1.dbo.StagingDeposit (
            deposit_id INTEGER IDENTITY(1,1) PRIMARY KEY,
            calendar_date varchar(max)  NULL,
            customer_email varchar(max)  NULL,
            customer_brand_name varchar(max)  NULL,
            customer_country varchar(max)  NULL,
            customer_account_status varchar(max)  NULL,
            payment_method_name varchar(max)  NULL,
            payment_method_type varchar(max)  NULL,
            payment_status_name varchar(max)  NULL,
            payment_status_description varchar(max)  NULL,
            amount_eur REAL NULL);
    
     CREATE TABLE question1.dbo.DepositTransaction (
            deposit_transaction_id  INTEGER IDENTITY(1,1) PRIMARY KEY,
            customer_id  INTEGER NOT NULL,
            payment_method_id   INTEGER NULL,
            payment_status_id   INTEGER  NULL,
            amount_eur REAL NULL,
            calendar_date varchar(max) NULL);       
    
     CREATE TABLE question1.dbo.GamePlayTransaction (
            gameplay_transaction_id  INTEGER IDENTITY(1,1) PRIMARY KEY,
            customer_id  INTEGER NOT NULL,
            provider_product_id  INTEGER NULL,
            device_name varchar(max) NULL,
            rounds INTEGER NULL,
            turnover  REAL NULL,
            game_win  REAL NULL,
            bonus_cost  REAL NULL,
            total_acc_revenue   REAL NULL,
            calendar_date varchar(max) NULL );    
    
     CREATE TABLE question1.dbo.Customer (
            customer_id  INTEGER IDENTITY(1,1) PRIMARY KEY,
            country_id  INTEGER NOT NULL,
            email varchar(max)  NULL,
            brand_name varchar(max)  NULL,
            account_status varchar(max)  NULL);      
    
     CREATE TABLE question1.dbo.PaymentMethod (
            payment_method_id   INTEGER IDENTITY(1,1) PRIMARY KEY,
            name varchar(max)  NULL,
            type varchar(max)  NULL);  
    
     CREATE TABLE question1.dbo.PaymentStatus (
            payment_status_id   INTEGER IDENTITY(1,1) PRIMARY KEY,
            name varchar(max)  NULL,
            description  varchar(max)  NULL);  
    
    
     CREATE TABLE question1.dbo.ProviderProduct (
            provider_product_id  INTEGER IDENTITY(1,1) PRIMARY KEY,
            product_name varchar(max)  NULL,
            provider_name varchar(max)  NULL);
    
     CREATE TABLE question1.dbo.Country (
            country_id  INTEGER IDENTITY(1,1) PRIMARY KEY,
            country_name varchar(max)  NULL);       
    
    
     ''')
    conn.commit()
