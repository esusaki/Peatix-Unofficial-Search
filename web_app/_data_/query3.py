import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# クエリ3
# ORDER BY
cursor.execute("SELECT title, start_date, pref FROM event WHERE start_date > '2024-11-04 18:00' AND start_date < '2024-11-04 23:00' ORDER BY start_date")
print(cursor.fetchall())
