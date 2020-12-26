import sqlite3



connection = sqlite3.connect("aquarium.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE stocks2 (name TEXT, tickers TEXT, date_number INTEGER)")

cursor.execute("INSERT INTO stocks2 VALUES ('Sammy', 'shark', 1)")
rows = cursor.execute("SELECT name, tickers  , date_number FROM stocks2").fetchall()
print(rows)
print(connection.total_changes)
