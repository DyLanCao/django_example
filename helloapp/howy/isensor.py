#!/usr/bin/env python
# encoding: utf-8

import random

#获取温度
def getTemperature():
    temp_min = 35
    temp_max = 37
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
        
def getmpu6050():
    x_alex_min = 1
    x_alex_max = 5
    y_alex_min = 1
    y_alex_max = 5
    z_alex_min = 1
    z_alex_max = 5
    while True:
        x_val = random.uniform(x_alex_min,x_alex_max)
        y_val = random.uniform(y_alex_min,y_alex_max)
        z_val = random.uniform(z_alex_min,z_alex_max)
        return round(x_val,0),round(y_val,0),round(z_val,0)


def getmax30100():
    heart_bit_min = 65
    heart_bit_max = 90
    bmp_min = 0.03
    bmp_max = 0.09
    while True:
        heart_bit = random.uniform(heart_bit_min,heart_bit_max)
        bmp_val = random.uniform(bmp_min,bmp_max)
        return round(heart_bit,1),round(bmp_val,4)
#温湿度
def getTemHum():
    result="体表温度: "+str(getTemperature())+"℃  空气湿度:"+str(getHumidity())+"%"
    return result

def getMpu():
    x_val,y_val,z_val = getmpu6050()
    #result="x_alix:" + str(x_val) + "y_alix:" + str(y_val) + "z_alix:" + str(z_val)
    result="x_alix speed up: " + str(x_val) + "mm" + "y_alix speed up: " + str(y_val) + "mm" + "z_alix speech up: " + str(z_val) + "mm"
    return result

def sleep_state():
    temp = getTemperature()
    if temp > 36.5:
        result="light sleep"
    else:
        result = "deep sleep"
    
    result1 = "the person sleep state is:" + result
    return result1

def getMax():
    heart_bit,bmp_val = getmax30100()
    result="average heart skiped:" + str(heart_bit) + "bleed  orygen:" + str(bmp_val)
    return result
