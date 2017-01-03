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

# Add a row of data.
conn.execute("INSERT INTO PRODUCT (ID, TITLE, PRICE) VALUES (1,"
             " 'The Pragmatic Programmer', 14.99 )")

# Add another row of data.
conn.execute("INSERT INTO PRODUCT (ID, TITLE, PRICE) VALUES (2, "
             "'The Self-taught Programmer', 14.59 )")

conn.commit()
conn.close()
