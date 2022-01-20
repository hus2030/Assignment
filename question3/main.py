import configparser
import pyodbc
from create_tables import create_dim,create_fact
from populate_dims import populate_dims
from populate_facts import populate_facts
config = configparser.ConfigParser()
config.read('connection.ini')

def main():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=' + config['DEFAULT']['Server']+
                          'Database=master;'
                          'Trusted_Connection=yes;')
   #Connecting to db and running all the functions
    create_dim(conn)
    create_fact(conn)
    populate_dims(conn)
    populate_facts(conn)
    print("Finished")


if __name__ == "__main__":
    main()
