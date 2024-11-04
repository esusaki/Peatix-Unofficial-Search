import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE pref (latitude INTEGER, longitude INTEGER, prefecture TEXT, PRIMARY KEY (latitude, longitude))")
conn.commit()
conn.close()