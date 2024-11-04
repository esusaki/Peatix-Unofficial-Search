import sqlite3
from extract_info import extract

def insert_event(id, title, start_date, pref, place):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM event WHERE id = ?;",(id,))
    count = cursor.fetchone()[0]

    if count != 0:
        print(f"すでに登録されているため、処理をスキップします。:{id}")
        return

    cursor.execute("INSERT INTO event (id, title, start_date, pref, place) VALUES (?, ?, ?, ?, ?);", (id, title, start_date, pref, place))
    conn.commit()
    conn.close()

def insert_keyword(event_id, keyword):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM keyword WHERE name = ?", (keyword,))
    result = cursor.fetchone()

    if  result == None:
        cursor.execute("INSERT INTO keyword (name) VALUES (?)", (keyword,)) 
        conn.commit()
        cursor.execute("SELECT * FROM keyword WHERE name = ?", (keyword,))
        result = cursor.fetchone()
    
    keyword_id = result[0]
    
    cursor.execute("INSERT INTO event_keyword (event_id, keyword_id) VALUES (?, ?)", (event_id, keyword_id))

    conn.commit()
    conn.close()

for _id_ in range(4110000, 4150000):

    result = extract(_id_)

    if result!=None:
        insert_event(result["id"], result["title"], result["start_date"], result["pref"], result["place"])

        for kw in result["keywords"]:
            insert_keyword(result["id"], kw)