import sqlite3
from sqlite3 import Error
# https://lucid.app/lucidchart/037c7067-c87a-4132-8268-8299d0494652/edit?beaconFlowId=1D5D81D3CCE07A60&page=BUMDxnZpKJ2k#
FILE = 'database.db'


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def insert(*args):
    conn = create_connection(FILE)

    try:
        cursor = conn.cursor()
        query = """INSERT INTO stock
                            (id, name, ticket, name, active) 
                            (?, ?, ?, ?)"""
        
        
    except Error as e:
        print(f'Error in database operation, {e}')
    finally:
        cursor.close()
        

