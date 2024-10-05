import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

#Query1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

#Query 2 
# cursor.execute('SELECT "Name" FROM "Artist"')

#query3
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

#query 4
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

#query 5
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

#query 6 
cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s', ["Queen"])

#fetch the results (multiple)
results = cursor.fetchall()

#fetch the results (single)
# results = cursor.fetchone() 

#close the connection
connection.close()

# print results
for result in results:
    print(result)