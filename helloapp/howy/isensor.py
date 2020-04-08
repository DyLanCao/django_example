#!/usr/bin/env python
# encoding: utf-8

import random

#获取温度
def getTemperature():
    temp_min = 15
    temp_max = 25
    while True:
        temp_val = random.uniform(temp_min,temp_max)
        return round(temp_val,1)
        
#获取湿度
def getHumidity():
    hum_min = 30
    hum_max = 50
    while True:
        temp_val = random.uniform(hum_min,hum_max)
        return round(temp_val,1)
        
#温湿度
def getTemHum():
    result="空气温度: "+str(getTemperature())+"℃  空气湿度:"+str(getHumidity())+"%"
    return result

print(getTemHum())
