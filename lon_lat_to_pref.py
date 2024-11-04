import requests
import json
import time
import sqlite3

def データベースで緯度経度から都道府県(緯度, 経度):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pref WHERE latitude = ? AND longitude = ?", (緯度, 経度))
    result = cursor.fetchone()

    return result

def データベースに緯度経度と都道府県の対応を登録(緯度, 経度, 都道府県):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pref (latitude, longitude, prefecture) VALUES (?,?,?)",(緯度, 経度, 都道府県))
    conn.commit()
    conn.close()

def 緯度経度から都道府県(緯度, 経度):

    データベースの問い合わせ結果 = データベースで緯度経度から都道府県(緯度, 経度)
    if データベースの問い合わせ結果 != None:
        都道府県 = データベースの問い合わせ結果[2]
    else:
        都道府県api_url = f"https://mreversegeocoder.gsi.go.jp/reverse-geocoder/LonLatToAddress?lat={緯度}&lon={経度}"
        response = requests.get(都道府県api_url)
        time.sleep(2)
        if "Proxy Error" in response.text:
            response = requests.get(都道府県api_url)
            time.sleep(2)
        response_dict = json.loads(response.text)
        if "results" not in response_dict:
            データベースに緯度経度と都道府県の対応を登録(緯度, 経度, None)
            return None
        else:
            muniCd = response_dict["results"]["muniCd"]
            都道府県 = None
            with open("municode.csv", encoding="utf-8") as f:
                rows = f.read().split("\n")
                for row in rows:
                    row2 = row.split(",")
                    if str(muniCd) in row2:
                        都道府県 = row2[2]
            データベースに緯度経度と都道府県の対応を登録(緯度, 経度, 都道府県)
    
    return 都道府県



