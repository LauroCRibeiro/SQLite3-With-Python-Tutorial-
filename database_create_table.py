#Done by Lauro Ribeiro (12/02/2021)

import sqlite3

#Tuturial 2 - Create a table

#Connect to database
conn = sqlite3.connect('customer.db')


#Create a cursor -- a cursor is what tells the database what we want to do.
c = conn.cursor()


#Create a table
c.execute("""CREATE TABLE customers(
        first_name text,
        last_name text,
        email text
    )""")



# Sqlite only has 5 Datatypes:
# NULL
# INTEGER
# REAL - (Decimal)
# TEXT
# BLOB - (Extraordinary file e.g-music file)


# Commit our command
conn.commit()

#Close our connection
conn.close()