import sqlite3
import os, sys

def 地方リスト():

    sys.path.append(os.path.abspath(os.path.dirname(__file__)))

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT chihou FROM prefecture;")

    chihoulist = [i[0] for i in cursor.fetchall()]

    if chihoulist[-1] == "オンライン":
        chihoulist = ["オンライン"] + chihoulist[:-1] 
    return chihoulist