#Done by Lauro Ribeiro (12/02/2021)

# Tutorial 7 - Use the Where Clause

import sqlite3

#Connect to database
conn = sqlite3.connect('customer.db')

#Create a cursor
c = conn.cursor()


#Query the database
c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com'")

items = c.fetchall()

for item in items:
    print(item)


#Commit our command
conn.commit()

#Close our connection
conn.close()
