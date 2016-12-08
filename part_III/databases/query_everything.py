import sqlite3

# Connect to your database.
conn = sqlite3.connect('my_store.db')

# Add a row of data.
data = conn.execute("SELECT* FROM PRODUCT")

for item in data:
    print(item)

conn.close()
