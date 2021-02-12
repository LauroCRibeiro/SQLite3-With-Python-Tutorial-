#Done by Lauro Ribeiro (12/02/2021)


# Tutorial 10 - Order results

import sqlite3

#Connect the database
conn = sqlite3.connect('customer.db')


#Create a cursor
c = conn.cursor()



#Query the database - Order by - In this case let's order the 1st names by ascending alphabetical order.
c.execute("SELECT rowid, * FROM customers ORDER BY first_name ASC")

items = c.fetchall()

for item in items:
    print(item)


# Commit our command
conn.commit()

#Close our command
conn.close()