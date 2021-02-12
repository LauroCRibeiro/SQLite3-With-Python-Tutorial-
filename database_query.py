#Done by Lauro Ribeiro (12/02/2021)

#Tutorial 4 - Query and fetchall

import sqlite3


#Connect to database
conn = sqlite3.connect('customer.db')


#Create a cursor
c = conn.cursor()


#Query the database
c.execute("SELECT * FROM customers")


#c.fetchone()
#c.fetchmany(3)
print(c.fetchall())



#Commit our command
conn.commit()

#Close our connection
conn.close()