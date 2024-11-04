import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# クエリ2
# 表結合, 集約演算, GROUP BY

cursor.execute("SELECT chihou, COUNT(*) FROM event, prefecture WHERE event.pref = prefecture.pref GROUP BY chihou")
print(cursor.fetchall())

