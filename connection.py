import sqlite3
from rich import print
# https://lucid.app/lucidchart/037c7067-c87a-4132-8268-8299d0494652/edit?beaconFlowId=1D5D81D3CCE07A60&page=BUMDxnZpKJ2k#

FILE = 'database.db'


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Cursor object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('Conexão criada!')
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print('Error in database connection: ', e)

    return cursor


def verify_stock(stock: str, date: str) -> str or bool :
    """Verify if have some register in database

    Args:
        stock (str): ticket of the stock
        date (str): date from stock

    Returns:
        str: price value
        bool: if not have any value
    """
    cursor: sqlite3.Cursor = create_connection(FILE)
    try:
        stock_id: int = 1 if 'B3SA3' in stock else 2
        cursor.execute(
            'SELECT * FROM price WHERE id_stock=? AND date=?', (stock_id, date))
        records: list = cursor.fetchone()
        if records:
            return records[3]
        else:
            return False
    except sqlite3.Error as e:
        print('Error in database verify: ', e)
    finally:
        cursor.close()


def insert(*args, **kargs):
    cursor = create_connection(FILE)

    try:
        query = """INSERT INTO stock
                            (id, name, ticket, name, active) 
                            (?, ?, ?, ?)"""

    except sqlite3.Error as e:
        print('Error in database operation: ', e)
    finally:
        cursor.close()
