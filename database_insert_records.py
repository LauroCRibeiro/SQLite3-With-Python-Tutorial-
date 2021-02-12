#Done by Lauro Ribeiro (12/02/2021)

#Insert many records

#Tutorial 3 - How to insert some Records

import sqlite3

#Connect to database
conn = sqlite3.connect('customer.db')


#Create a cursor
c = conn.cursor()


many_customers = [

                    ('Lauro', 'Ribeiro', 'lauroribeiro@gmail.com'),
                    ('Victor Hugo', 'dos Santos', 'hugosantos@gmail.com'),
                    ('Wes', 'Brown', 'wes@brown.com'),
                    ('Mary', 'Holland', 'maryholland@gmail.com'),
                    ('Molly', 'Peters', 'mollypeters@gmail.com')

                ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)



print("Command executed successfully...")


#Commit our command
conn.commit()

#Close our connection
conn.close()