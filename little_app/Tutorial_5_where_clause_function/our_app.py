import database_where

# Add a record to the database
#database_add.add_one("Melanie","Thierry","melaniethierry@gmail.com")


# Delete a Record - use the rowid as a string
#database_delete.delete_one('8')


# Lookup Email Address Record
database_where.email_lookup("%@gmail.com")


# Add many Records

'''
stuff = [
    ('Milou','Sluis','milousluis@hotmail.com'),
    ('Claudia','Schiffer','claudias@gmail.com')

    ]

database_where.add_many(stuff)
'''



# Show all the records
database_where.show_all()