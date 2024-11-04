from flask import Flask, render_template, request, url_for
#from web_app._data_.地方リスト import 地方リスト
import os, sys

app = Flask(__name__, static_folder="./static/")

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from _data_._filter_ import filter
from _data_.地方リスト import 地方リスト

@app.route("/", methods = ["GET","POST"])
def home():
    result = False

    keywords_for_checkbox = ["働き方","起業","キャリア","ワークライフバランス","メディカル／ヘルスケア","社会貢献／地域活性","医療","地域活性",
                            "テクノロジー／サイエンス","子育て","ものづくり","まちづくり","音楽／ライブ／フェス","イノベーション","ウェルビーイング"]
    
    if request.method == "POST":

        keywords_checked = []

        for kw in keywords_for_checkbox:
            if kw in request.form:
                keywords_checked.append(kw)
        
        チェックされている地方 = []
        for 地方 in 地方リスト():
            if 地方 in request.form:
                チェックされている地方.append(地方)

        result = (filter(date_min=request.form["date_min"], date_max=request.form["date_max"], keywords = keywords_checked, places=チェックされている地方))

        default_form_value = request.form
    else:
        default_form_value = {"date_min":None, "date_max":None}
    
    if result == False:
        result_count = False
    else:
        result_count = len(result)

    return render_template("home.html", keywords_for_checkbox = keywords_for_checkbox, result = result, result_count = result_count, default_form_value = default_form_value, places_for_checkbox = 地方リスト())

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

if (__name__ == "__main__"):
    app.run(debug = True)