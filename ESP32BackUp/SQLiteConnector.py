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

    
def create_Data_Inserter(conn, task):
    sql = ''' INSERT INTO measuredData(TEMP, HUMD, SMOKE, XLOCATION, YLOCATION)
                VALUES(?,?,?,?,?) 	'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid
def main():
    database = r"~/IOT2-Projekt/Database/measuredData.db"
    
    conn = create_connection(database)
    with conn:
        task_1 =(msg)
        create_task(conn, task_1)
if __name__ == '__man__':
    create_connection(r"~/IOT2-Projekt/Database/measuredData.db")
    main()