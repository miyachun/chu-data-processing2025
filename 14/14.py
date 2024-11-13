import json,urllib.request
from flask import Flask, render_template
import requests

import json,urllib.request
import re


app = Flask(__name__)
myD={'city':[],'strT':[],'endT':[]}
  
@app.route('/')
def index():
    
    url = 'https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/59/5776ed30-fa3c-48f4-9876-d8fb28df0501.json?1130722174700'

    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
   
    for i in output:
        #print(i)
        name = i['站點名稱']        
        sT=i['站點位置']
        sTP=i['圖片']
        #a=strT+city
        myD['city'].append(name)
        myD['strT'].append(sT)
        myD['endT'].append(sTP)
        
    return render_template('index.html',a=myD)


if __name__ == '__main__':
    app.run()
