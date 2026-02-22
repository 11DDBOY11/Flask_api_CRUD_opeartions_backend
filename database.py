import sqlite3
DATABASE='mydb.db'
def get_db():
    conn=sqlite3.connect(DATABASE)
    conn.row_factory=sqlite3.Row
    return conn

def create_student():
    conn=get_db() 
    conn.execute(""" create table if not exists students (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name VARCHAR(50) NOT NULL,
                 email VARCHAR(50) UNIQUE NOT NULL,
                 course VARCHAR(50) NOT NULL)""")
    conn.commit()
    conn.close()