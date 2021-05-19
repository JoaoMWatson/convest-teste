import sqlite3
from rich import print
# https://lucid.app/lucidchart/037c7067-c87a-4132-8268-8299d0494652/edit?beaconFlowId=1D5D81D3CCE07A60&page=BUMDxnZpKJ2k#

FILE = 'database.db'


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connect object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('Successfully Connected !')
    except sqlite3.Error as e:
        print('Error in database connection: ', e)

    return conn


def verify_price_stock(stock: str, date: str) -> bool:
    """Verify if have some register in database

    Args:
        stock (str): ticket of the stock
        date (str): date of operation

    Returns:
        bool: True if has a value False if not.
    """
    conn = create_connection(FILE)
    cursor: sqlite3.Cursor = conn.cursor()
    try:
        stock_id: int = 1 if 'B3SA3' in stock else 2
        cursor.execute(
            'SELECT * FROM price WHERE id_stock=? AND date=?', (stock_id, date))
        records: list = cursor.fetchone()
        if records:
            return True
        else:
            return False
    except sqlite3.Error as e:
        print('Error in database verify: ', e)
    finally:
        cursor.close()


def insert(*args, **kargs):
    conn = create_connection(FILE)
    cursor: sqlite3.Cursor = conn.cursor()
    stock_id: int = 1 if 'B3SA3' in args['stock'] else 2
    
    is_register: bool = verify_price_stock(args['stock'], args['date'])
    
    try:
        if not is_register:
            insert_stock = """INSERT INTO stock
                                (ticket, name, active) 
                                VALUES
                                (?, ?, ?, ?)"""

            insert_price = """INSERT INTO price 
                                (id_stock, date, price)
                                VALUES
                                (?, ?, ?)
                            """

            cursor.executem(insert_stock, (args['stock'], args['stock']))
            cursor.executem(insert_price, (stock_id, args['date'], args['price']))

    except sqlite3.Error as e:
        print('Error in database operation: ', e)
    finally:
        cursor.close()
