###Imports
import sqlite3
from sqlite3 import Error

def create_connection(measuredData.db):
    conn = None
    try:
        conn = sqlite3.connect(measuredData.db)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
if __name__ == '__man__':
    create_connection(r"~/IOT2-Projekt/Database/measuredData.db")