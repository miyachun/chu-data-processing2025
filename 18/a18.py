#https://fhy.wra.gov.tw/WraApi#
#https://fhy.wra.gov.tw/WraApi#!/WaterApi/WaterApi_RealTimeInfo

import requests
import json
from flask import Flask, render_template


app = Flask(__name__)
myD={'StationNo':[],'Time':[],'WaterLevel':[]}
  
@app.route('/')
def index():
    
    url = 'https://fhy.wra.gov.tw/WraApi/v1/Water/RealTimeInfo?$top=30'

    response = requests.get(url=url)
    

    text = response.text
    #print(text)

    json_loads = json.loads(text)

    myD={'StationNo':[],'Time':[],'WaterLevel':[]}
    
    for i in json_loads:
        #print(i)
        StationNo = i['StationNo']        
        Time=i['Time']
        WaterLevel=i['WaterLevel']
        #a=strT+city
        myD['StationNo'].append(StationNo)
        myD['Time'].append(Time)
        myD['WaterLevel'].append(WaterLevel)

        
    return render_template('index.html',a=myD)


if __name__ == '__main__':
    app.run()