#Done by Lauro Ribeiro (12/02/2021)


# Tutorial 12 - Limiting Results

import sqlite3

#Connect to database
conn = sqlite3.connect('customer.db')


#Create a cursor
c = conn.cursor()


# Query the database -limit the results
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

items = c.fetchall()

for item in items:
    print(item)



# Commit our command
conn.commit()

# Close our command
conn.close()
