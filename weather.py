#!/usr/bin/env python
# coding: utf-8


import requests
import json
import pymysql
import threading
def func():
	response = requests.get("https://free-api.heweather.net/s6/weather/now?location=CN101043700&key=1d2b6085438f45529a262c4f8ac1c639")
	data = json.loads(response.text).get('HeWeather6')[0].get('now') # 获取当前气象数据
	tmp = data.get('tmp') #温度
	hum = data.get('hum') #湿度
	cond_txt = data.get('pcpn') #当前天气状况
	wind_deg = data.get('wind_deg') #风向 360度
	wind_dir = data.get('wind_dir') #风向
	wind_sc = data.get('wind_sc') #风力
	pres = data.get('pres') #气压
	time_data = json.loads(response.text).get('HeWeather6')[0].get('update').get('loc') #当前时间
	connection = pymysql.connect(host='localhost',user='root',password='12345678yY',db='weather')
	cursor = connection.cursor()
	cursor.execute("insert into wea_data values(null,%s,%s,%s,%s,%s,%s,%s,%s)",(time_data,tmp,hum,cond_txt,wind_deg,wind_dir,wind_sc,pres))
	connection.commit()
	timer = threading.Timer(5,func)
	timer.start()

func()
  	

	







