import requests
import os
import time
import datetime

def save_page(target_id, skip_already_saved = True):
    print(target_id)

    save_folder = "saved_pages"

    export_path = f"{save_folder}/{target_id}.html"

    if skip_already_saved == True:
        if os.path.exists(export_path):
            return

    target_url = f"https://peatix.com/event/{target_id}"

    try:
        response = requests.get(target_url)
        response.encoding = response.apparent_encoding
    except:
        time.sleep(10)
        response = requests.get(target_url)
        response.encoding = response.apparent_encoding

    with open(export_path, mode="w", encoding="utf-8") as f:
        f.write(response.text)
    
    with open(f"{save_folder}/last_fetched_time/{target_id}.txt", mode = "w", encoding="utf-8") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    
    time.sleep(5)

for id in range(4150000, 4180000):
    save_page(id)
