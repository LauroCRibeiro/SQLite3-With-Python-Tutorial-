#Done by Lauro Ribeiro (12/02/2021)

import sqlite3

#Tutorial app 1 - Show All Function

# Query the database and Return All Records
def show_all():
    # Connect to database
    conn = sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()

    #Query the Database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    #Commit our command
    conn.commit()
    #Close our connection
    conn.close()



