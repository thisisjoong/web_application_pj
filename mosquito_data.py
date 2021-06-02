import requests
import json

def get_mosquito_data(day):

    # KEY = '/664a465953617366343553566c6e46'
    # TYPE =  '/json'
    # SERVICE = '/MosquitoStatus'
    # START_INDEX = '/1'
    # END_INDEX = '/5'
    # MOSQUITO_DATE = ''
    # url = 'http://openapi.seoul.go.kr:8088' + KEY +TYPE + SERVICE+ START_INDEX+ END_INDEX + '/' + datetime(MOSQUITO_DATE)
    day = day
    url = 'http://openapi.seoul.go.kr:8088/664a465953617366343553566c6e46/json/MosquitoStatus/1/5/' + day
    res = requests.get(url)

    # print(res.url)
    # print(res.text)
    
    data = json.loads(res.text)
    #print(data, type(data))

    return data
