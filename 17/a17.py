#https://fhy.wra.gov.tw/WraApi
#url='https://fhy.wra.gov.tw/WraApi/v1/Water/Station?$top=30'


#import xmlschema
url = "https://fhy.wra.gov.tw/WraApi/v1/Water/Station?$top=30"
#my_schema = xmlschema.XMLSchema('Station.xml')

import xml.etree.ElementTree as ET

import requests


tree=ET.parse('Station.xml')
root=tree.getroot()
#element=root.findall('WaterStation')

for _id in root.findall('WaterStation'):
        Sno = _id.find('StationNo').text
        Sname = _id.find('StationName').text
        L1=_id.find('WarningLevel1').text
        L2=_id.find('WarningLevel2').text
        print(Sno,Sname,L1,L2)











