#Done by Lauro Ribeiro (12/02/2021)

#Primary key - Just prints the number id in each contact inserted in the database.

#Tutorial 6

import sqlite3

#Connect to the database
conn = sqlite3.connect('customer.db')


#Create a cursor
c = conn.cursor()


#Query the database
c.execute("SELECT rowid, * FROM customers")
#c.fetchone()
#c.fetchmany(3)

items = c.fetchall()

for item in items:
    print(item)

#Commit our command 
conn.commit()

#Close our command 
conn.close()