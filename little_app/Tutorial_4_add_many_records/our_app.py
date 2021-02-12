import database_many

# Add a record to the database
#database_add.add_one("Melanie","Thierry","melaniethierry@gmail.com")


# Delete a Record - use the rowid as a string
#database_delete.delete_one('8')



# Add many Records


stuff = [
    ('Milou','Sluis','milousluis@hotmail.com'),
    ('Claudia','Schiffer','claudias@gmail.com')

    ]

database_many.add_many(stuff)




# Show all the records
database_many.show_all()