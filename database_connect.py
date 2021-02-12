#Done by Lauro Ribeiro (12/02/2021)

# Tuturial 1- Connect to database in python

#Create SQLite Connection

import sqlite3


#Create a connector- connect to database
conn = sqlite3.connect('customer.db')

print("Opening database...")