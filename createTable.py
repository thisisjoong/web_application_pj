import sqlite3
import json
import requests

with open('C:/Users/KHJ/section 3 project/data.json', 'rt', encoding= 'UTF8') as json_file:
    myjson = json.load(json_file)
conn = sqlite3.connect('mydb.db')

c= conn.cursor()

c.execute("CREATE TABLE mosquito_data(mosquito_date varchar(2000), mosquito_value_water varchar(2000), mosquito_value_house varchar(2000), mosquito_value_park varchar(2000))")


myData =[]

for data_dict in myjson:
    t = (data_dict['mosquito_date'], data_dict['mosquito_value_water'], data_dict['mosquito_value_house'], data_dict['mosquito_value_park'])
    myData.append(t)

c.executemany("INSERT INTO mosquito_data(mosquito_date, mosquito_value_water,mosquito_value_house,mosquito_value_park) VALUES (?,?,?,?)",myData)


conn.commit()
conn.close()
