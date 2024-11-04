import sqlite3

def 地方リスト():

    conn = sqlite3.connect("_data_/data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT chihou FROM prefecture;")

    chihoulist = [i[0] for i in cursor.fetchall()]

    if chihoulist[-1] == "オンライン":
        chihoulist = ["オンライン"] + chihoulist[:-1] 
    return chihoulist