import sqlite3

def create_table_event():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS event;")
    cursor.execute("CREATE TABLE event (id INTEGER PRIMARY KEY, title TEXT, start_date DATETIME, pref TEXT, place TEXT);")

    cursor.execute("DROP TABLE IF EXISTS prefecture;")
    cursor.execute("CREATE TABLE prefecture (pref TEXT PRIMARY KEY,  chihou TEXT);")

    cursor.execute("DROP TABLE IF EXISTS keyword;")
    cursor.execute("CREATE TABLE keyword (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);")
    
    cursor.execute("DROP TABLE IF EXISTS event_keyword;")
    cursor.execute("CREATE TABLE event_keyword (event_id INTEGER, keyword_id INTEGER, PRIMARY KEY (event_id, keyword_id), FOREIGN KEY (event_id) REFERENCES event(id), FOREIGN KEY (keyword_id) REFERENCES keyword(id));")

    conn.commit()
    conn.close()

create_table_event()