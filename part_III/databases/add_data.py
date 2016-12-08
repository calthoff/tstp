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
