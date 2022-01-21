from queries import view
from create import create_tables ,create_database
from staging import staging_fill
from populate import populate_tables
import pyodbc
import configparser
config = configparser.ConfigParser()
config.read('connection.ini')

def main():

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=' + config['DEFAULT']['Server']+
                          'Database=master;'
                          'Trusted_Connection=yes;',autocommit=True)
    deposit_link = config['DEFAULT']['deposit_link']
    gameplay_link = config['DEFAULT']['gameplay_link']

    print("Creating database question1...")
    create_database(conn)
    print("Creating staging tables...")
    create_tables(conn)
    print("Populating staging tables...")
    staging_fill(conn, deposit_link, gameplay_link)
    print("Populating main tables...")
    populate_tables(conn)
    # Viewing results
    view(conn)
    # Closing connection
    conn.close() 
        
if __name__ == "__main__":
    main()
