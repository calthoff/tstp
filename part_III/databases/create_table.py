import sqlite3

# Connect to your database.
conn = sqlite3.connect('my_store.db')

# Create a table.
conn.execute("""
       CREATE TABLE PRODUCT
       (ID INT PRIMARY KEY NOT NULL,
       TITLE TEXT NOT NULL,
       PRICE INT NOT NULL);
       """)

conn.close()
