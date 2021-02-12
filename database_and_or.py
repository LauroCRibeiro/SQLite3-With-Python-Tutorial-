#Done by Lauro Ribeiro (12/02/2021)

# Tutorial 11 - AND/OR


import sqlite3 

#Connect the database
conn = sqlite3.connect('customer.db')


#Create a cursor
c = conn.cursor()



#Query the database - AND/OR
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE '%Ribeiro' \
        AND  email LIKE '%gmail.com'")  #Instead of 'AND' we could've used 'OR' in case we wanted 
                                          #to identify a true and a false variable.
items = c.fetchall()

for item in items:
    print(item)


# Commit our command
conn.commit()

# Close our command
conn.close()