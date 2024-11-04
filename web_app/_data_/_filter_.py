import sqlite3
import datetime

def current_date():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, "%Y-%m-%d %H:%M")

def filter(keywords, date_min, date_max, places):
    conn = sqlite3.connect("_data_/data.db")
    cursor = conn.cursor()

    if date_min == False or date_min == "":
        option_query_1 = f"start_date > '{current_date()}'"
    else:
        option_query_1 = f"start_date > '{date_min} 00:00'"

    if date_max == False or date_max == "":
        option_query_2 = ""
    else:
        option_query_2 = f"AND start_date < '{date_max} 23:59'"
    
    if keywords == []:
        option_query_3 = ""
    else:
        option_query_3 = f"AND id IN (SELECT event_id FROM keyword, event_keyword WHERE id = keyword_id AND name IN ({'"' + '","'.join(keywords) + '"'}))"

    if places == []:
        option_query_4 = ""
    else:
        option_query_4 = f"AND pref IN (SELECT pref FROM prefecture WHERE chihou IN ({'"' + '","'.join(places) + '"'}))"

    cursor.execute(f"SELECT * FROM event WHERE {option_query_1} {option_query_2} {option_query_3} {option_query_4} ORDER BY start_date")
    return cursor.fetchall()
