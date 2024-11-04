import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

#cursor.execute("SELECT * FROM event, event_keyword WHERE id = event_id AND start_date > ? AND keyword IN ('教育','エンジニア','まちづくり')", ("2024-10-22 0:00",))

cursor.execute("SELECT keyword, COUNT(*) as keyword_count FROM event_keyword GROUP BY keyword ORDER BY keyword_count DESC")

print(cursor.fetchall())