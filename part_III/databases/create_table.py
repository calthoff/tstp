# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

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
