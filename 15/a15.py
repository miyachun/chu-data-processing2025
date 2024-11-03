import json,urllib.request
from flask import Flask, render_template
import requests

import json,urllib.request
import re


app = Flask(__name__)
myD={'name':[],'area':[],'addr':[],'time':[]}
  
@app.route('/')
def index():
    
    url = 'https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/68/9813f5cd-6686-4047-b6eb-609d163286f8.json?1130726160042'

    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
   
    for i in output:
        #print(i)
        name = i['加油站名']        
        area=i['行政區']
        addr=i['住址']
        time=i['營業時間']
        #a=strT+city
        myD['name'].append(name)
        myD['area'].append(area)
        myD['addr'].append(addr)
        myD['time'].append(time)
        
    return render_template('index.html',a=myD)


if __name__ == '__main__':
    app.run()