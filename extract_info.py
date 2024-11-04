import os
from bs4 import BeautifulSoup
import re
from lon_lat_to_pref import 緯度経度から都道府県

def extract(target_id):
    save_path = f"saved_pages/{target_id}.html"

    if os.path.exists(save_path) == False:
        print(f"エラー:ファイルが存在しません '{save_path}'")
        return
    
    if os.path.exists(f"saved_pages/last_fetched_time/{target_id}.txt") == False:
        print(f"エラー:取得日時のファイルが存在しません")
        return

    with open(save_path, encoding="utf-8") as f:
        target_text = f.read()
    
    if target_text == "":
        print(f"Page Not Found:{target_id}")
        return
    
    soup = BeautifulSoup(target_text, "html.parser")
    title = soup.find(property = "og:title")["content"]

    if title == "Peatix: Tools for Communities and Events":
        print(f"Page Not Found:{target_id}")
        return

    if title == "Authorization required":
        print(f"このイベントはパスワードで保護されており見られません: {target_id}")
        return
    
    # htmlファイルが存在し、かつ、page not foundでもない場合の処理

    start_date = soup.find(itemprop = "startDate")["content"].replace("T"," ")

    keywords_pattern = r'\"peatix_tag\":\[.*?\]'
    keywords_text = re.findall(keywords_pattern, target_text)

    if len(keywords_text) != 1:
        print(f"エラー:キーワードのリストの長さが1ではありません:{keywords_text}")
        return
    
    keywords = keywords_text[0].split('[')[1].rstrip("]").split(",")
    keywords = [i.strip('"') for i in keywords]

    place_str = ""
    place = soup.find(itemtype = "http://schema.org/Place")
    for meta in place.find_all("meta"):
        if meta["itemprop"] in ["name","address"]:
            place_str += meta["content"] + " "
    place_str = place_str.strip()

    pref = None

    if place_str == "オンライン":
        pref = "オンライン"
    else:
        GeoCoordinates = soup.find(itemtype = "http://schema.org/GeoCoordinates")

        if GeoCoordinates == None:
            print("error! 対面開催ですが、緯度経度の情報がありません", target_id)
        else:

            print(place_str)
            for meta in GeoCoordinates.find_all("meta"):
                if meta["itemprop"] == "latitude":
                    latitude = meta["content"]
                elif meta["itemprop"] == "longitude":
                    longitude = meta["content"]
                
            if latitude == None or longitude == None:
                print("error! 緯度経度の情報がありません", target_id)
                exit()
            else:
                pref = 緯度経度から都道府県(latitude, longitude)

    with open(f"saved_pages/last_fetched_time/{target_id}.txt") as f:
        last_fetched_time_str = f.read()

    return {"id":target_id,"title":title, "start_date":start_date, "keywords":keywords, "pref":pref, "last_fetched":last_fetched_time_str, "place":place_str}

#for id in range(4150000, 4165000):
#    print(extract(id))