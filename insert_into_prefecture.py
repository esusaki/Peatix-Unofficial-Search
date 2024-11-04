import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM prefecture;")

with open("todoufuken-chihou.csv", encoding="utf-8") as f:
    都道府県_地方 = [i.split(",") for i in  f.read().split("\n")]

    for i in 都道府県_地方:
        cursor.execute("INSERT INTO prefecture (pref, chihou) VALUES (?, ?)", i)

cursor.execute("INSERT INTO prefecture (pref, chihou) VALUES (?, ?)", ("オンライン","オンライン"))

conn.commit()