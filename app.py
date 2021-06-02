from flask import Flask , render_template
import mosquito_data
from datetime import date, timedelta
from flask import json as fJson
import requests
import json
import sqlite3


# 앱 생성
app = Flask(__name__)

# url 라우터
@app.route('/')
def index():

    now= date.today()
    now_str = str(now)
    print(now_str)

    #오늘날짜로 요청
    data = mosquito_data.get_mosquito_data(now_str)
    print(data)
    #없으면 어제 날짜로 요청
    if not data:
        yesterday = now - timedelta(days=1)
        yesterday_str = str(yesterday)
        print(yesterday_str)

        data = mosquito_data.get_mosquito_data(yesterday_str)
        print(data)
    
    return render_template('index.html', data=data)

# @app.route('/second', methods=['GET', 'PATCH'])
# def history():
# # with statement
#     with open('C:/Users/KHJ/section 3 project/data.json', 'rt', encoding= 'UTF8') as json_file:
#         json_data = json.load(json_file)
#         #json2html.convert = (json = json_data)
#     return render_template('second.html', title="page", jsonfile=json.dumps(json_data), data=json_data)

@app.route("/third", methods=['GET'])
def history():
	conn = sqlite3.connect('mydb.db')
	conn.row_factory=sqlite3.Row
	c = conn.cursor()
	c.execute('SELECT mosquito_date, mosquito_value_water, mosquito_value_house, mosquito_value_park FROM mosquito_data')
	rows = c.fetchall(); 
	return render_template("third.html",rows = rows )

@app.route("/chart",methods=['GET'])
def today_chart():
    now= date.today()
    now_str = str(now)
    print(now_str)

    #오늘날짜로 요청
    data = mosquito_data.get_mosquito_data(now_str)
    print(data)
    #없으면 어제 날짜로 요청
    if not data:
        yesterday = now - timedelta(days=1)
        yesterday_str = str(yesterday)
        print(yesterday_str)

        data = mosquito_data.get_mosquito_data(yesterday_str)
        print(data)
    return render_template("chart.html", data = data)

#메인 영역
if __name__ == '__main__':
    app.run(debug=True)

