import database_delete

# Add a record to the database
#database_add.add_one("Melanie","Thierry","melaniethierry@gmail.com")


# Delete a Record - use the rowid as a string
database_delete.delete_one('8')


# Show all the records
database_delete.show_all()