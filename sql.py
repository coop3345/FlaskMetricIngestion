import sqlite3

####################################################################
## Quick python script you can run to verify that the flask server is populating the two tables configured for ingestion.
####################################################################

conn = sqlite3.connect("bazaar.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Auth ORDER BY Timestamp DESC LIMIT 5;")
Auth = cursor.fetchall()
cursor.execute("SELECT * FROM Basement ORDER BY Timestamp DESC LIMIT 5;")
Basement = cursor.fetchall()

print(Auth)
print(Basement)
