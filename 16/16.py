import json,urllib.request
from flask import Flask, render_template,request
import requests

import json,urllib.request
import re


app = Flask(__name__)
myD={'name':[],'area':[],'addr':[],'time':[]}
myD01={'name':[],'area':[],'addr':[],'time':[]}  
@app.route('/',methods=('GET','POST'))
def index():
    global myD
    global myD01 
    url = 'https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/68/9813f5cd-6686-4047-b6eb-609d163286f8.json?1130726160042'

    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    if request.method == 'POST':
        
        myD01.clear()
        myD01={'name':[],'area':[],'addr':[],'time':[]} 
        dropdownval=request.form.get('colour')
        print(dropdownval)
           
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
            if dropdownval in area:
                myD01['name'].append(area)
                myD01['area'].append(name)
                myD01['addr'].append(addr)
                myD01['time'].append(time)
          
        return render_template('index.html',a=myD,b=myD01,c='0')
    else:
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
        return render_template('index.html',a=myD,b=myD01,c='1')

if __name__ == '__main__':
    app.run()
