#Done by Lauro Ribeiro (12/02/2021)

#Tutorial 5 - Format your results

import sqlite3


#Connect to database
conn = sqlite3.connect('customer.db')


#Create a cursor
c = conn.cursor()


#Query the database
c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany(3)

items = c.fetchall()

print("NAME " + "\t\tEMAIL")
print("-------" + "\t\t--------")
for item in items:
    print(item[0] + " " + item[1] + "\t\t" + item[2])



#Commit our command
conn.commit()

#Close our connection
conn.close()


