from flask import Flask, render_template, request
import webbrowser
import json
from . import apis
from . import sort_json
from .config import URL, DEFAULT_CENTER_LATLNG

app = Flask(__name__)
# index.htmlの自動起動
webbrowser.open(URL)


@app.route("/index")
def index():
    center_latlng = DEFAULT_CENTER_LATLNG
    return render_template("index.html", center_latlng=center_latlng)


@app.route("/search", methods=["post"])
def search():
    # 中心地
    center_address = request.form["center_address"]
    center_latlng = apis.get_center_latlng(center_address)
    center_latlng_str = json.dumps(center_latlng)
    print("center_latlng: ", center_latlng_str)

    restaurants = request.form["restaurants"]
    restaurants_dic = apis.gurunavi_info(center_latlng, restaurants)
    if restaurants_dic == False:
        return render_template("index.html", center_latlng=center_latlng_str)
    else:
        result = restaurants_dic["rest"]
        lis = []
        # json文字列の作成
        for i in range(len(result)):
            restaurant_latlng = {}
            restaurant_latlng["lat"] = float(result[i]["latitude"])
            restaurant_latlng["lng"] = float(result[i]["longitude"])
            print("restaurants_latlng: ", restaurant_latlng)
            dic = {}
            dic["name"] = result[i]["name"]
            dic["latlng"] = restaurant_latlng
            distance_info = apis.get_distance(
                center_address, result[i]["name"])
            if distance_info == False:
                center_latlng = ' { "lat": 35.91745969999999, "lng": 139.9064798 }'
                return(render_template("index.html", center_latlng=center_latlng_str))
            dic["distance"] = distance_info["distance"]["value"]
            dic["duration"] = distance_info["duration"]["text"]
            dic["lunch_price"] = result[i]["lunch"]
            dic["parking"] = result[i]["parking_lots"]
            dic["url"] = result[i]["url"]
            dic["img"] = result[i]["image_url"]["shop_image1"]
            lis.append(dic)
        # print("lis: ",lis)
        priority = request.form["priority"]
        if priority == "distance":
            order = "up"
        elif priority == "lunch_price":
            order = "up"
        elif priority == "parking":
            order = "down"

        sorted_json = sort_json.sort_json(lis, priority, order)
        sorted_json_str = json.dumps(sorted_json)

        return render_template("index.html", center_latlng=center_latlng_str, restaurants_str=sorted_json_str)


if __name__ == "__main__":
    app.run(debug=True)
