from queries import view
from create import create_tables
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
                          'Trusted_Connection=yes;')
    deposit_link = config['DEFAULT']['deposit_link']
    gameplay_link = config['DEFAULT']['gameplay_link']

    print("Creating staging tables...")
    create_tables(conn)
    print("Populating staging tables...")
    staging_fill(conn, deposit_link, gameplay_link)
    print("Populating main tables...")
    populate_tables(conn)
    view(conn)

if __name__ == "__main__":
    main()