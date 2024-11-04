import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# クエリ1
# 表結合, 入れ子型問い合わせ

cursor.execute("SELECT title FROM event WHERE start_date > '2024-11-05 00:00' AND id IN (SELECT event_id FROM keyword, event_keyword WHERE id = keyword_id AND name IN (?, ?));", ("テクノロジー","DX"))
print(cursor.fetchall())