#imports
import requests;
import pandas as pd;
from flask import Flask, request, jsonify;
import joblib;
#reading longitude and lattitude data from csv file
df=pd.read_csv(r'C:\Users\Umang\Desktop\React-Native\GeoLocationDemo\server\data.csv');

#converting it to dictionary format
listofdic=df.to_dict(); 
  
#list of lattitudes and longitudes              
lattitudes=[];
longitudes=[];
for i in listofdic['lat']:
    lattitudes.append(listofdic['lat'][i]);
for i in listofdic['lng']:
    longitudes.append(listofdic['lng'][i]);

#getting data from openweathermapapi
listofjsondata=[];
for i in range(0,len(lattitudes)):
    response=requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lattitudes[i]}&lon={longitudes[i]}&appid=db112d3739aa9252822907ef98be86ad");
    listofjsondata.append(response.json());

var1=[];
for i in range(0,len(listofjsondata)):
    var1.append(listofjsondata[i]['coord'])

var2=[];
for i in range(0,len(listofjsondata)):
    for j in range(0,len(listofjsondata[i]['list'])):
        var2.append(listofjsondata[i]['list'][j]['components']);

df1 = pd.DataFrame(var1)
df2 = pd.DataFrame(var2)
result=pd.concat([df1,df2],axis=1);
print(result);