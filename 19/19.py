#https://data.gov.tw/dataset/109336
#https://data.gov.tw/dataset/67491
import json,urllib.request
from flask import Flask, render_template,request,url_for, flash, redirect, abort
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_bootstrap import Bootstrap
import requests
import sqlite3
import datetime

app = Flask(__name__)
myD={'Tarea':[],'Taddr':[],'Ttype':[],'Tspeed':[]}
myD01={'Tarea':[],'Taddr':[],'Ttype':[],'Tspeed':[]}
myD02={'Tarea':[],'Tspeed':[],'lon':[],'lat':[]}         
c='1'


@app.route('/list')
def list():   
             
        with open('1d103aa0-d3c1-400b-8a18-76076df42013.json', 'r',encoding='utf-8') as file:
            data = json.load(file)
    
            for i in data:
                
                Tarea=i['地點']
                Tspeed= i['速限']
                lon=i['經度']
                lat=i['緯度']               

                #a=strT+city
                myD02['Tarea'].append(Tarea)
                myD02['Tspeed'].append(Tspeed)
                myD02['lon'].append(lon)        
                myD02['lat'].append(lat)

        return render_template('list.html',a=myD02)  




@app.route('/',methods=('GET','POST'))
def index():
    global myD
    global myD01
    global c   
    if request.method == 'POST':
        c='0'
        myD01.clear()
        myD01={'Tarea':[],'Taddr':[],'Ttype':[],'Tspeed':[]}   
        dropdownval=request.form.get('colour')
        print(dropdownval)
 
        # Open and read the JSON file
        with open('5bceaf01-c0a4-4848-9602-0b3fd804faa2.json', 'r',encoding='utf-8') as file:
            data = json.load(file)
    
            for i in data:
                
                Tarea=i['轄區分局']
                Taddr = i['設置地點']
                Ttype=i['取締類型']
                Tspeed=i['測速時速限制']               

                #a=strT+city
                myD['Tarea'].append(Tarea)
                myD['Taddr'].append(Taddr)
                myD['Ttype'].append(Ttype)        
                myD['Tspeed'].append(Tspeed)
                if dropdownval in Tarea:
                    myD01['Tarea'].append(Tarea)
                    myD01['Taddr'].append(Taddr)
                    myD01['Ttype'].append(Ttype)
                    myD01['Tspeed'].append(Tspeed)

                        
            return render_template('index.html',a=myD,b=myD01,c=c)
    else:
        myD01.clear()       
        with open('5bceaf01-c0a4-4848-9602-0b3fd804faa2.json', 'r',encoding='utf-8') as file:
            data = json.load(file)
    
            for i in data:
                
                Tarea=i['轄區分局']
                Taddr = i['設置地點']
                Ttype=i['取締類型']
                Tspeed=i['測速時速限制']               

                #a=strT+city
                myD['Tarea'].append(Tarea)
                myD['Taddr'].append(Taddr)
                myD['Ttype'].append(Ttype)        
                myD['Tspeed'].append(Tspeed)

        return render_template('index.html',a=myD,b=myD01,c=c)        


if __name__ == '__main__':
    app.run()