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
data = conn.execute("SELECT* FROM PRODUCT WHERE title='The Pragmatic Programmer' AND  price > 14.9")

for item in data:
    print(item)

conn.close()
