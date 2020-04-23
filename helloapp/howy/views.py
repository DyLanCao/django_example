
from distutils.command import register
 
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse

from . import isensor

'''
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context) 
'''

def hello(request):
    tem = isensor.getTemHum()
    tes = isensor.getMpu()
    tss = isensor.getMax()
    sleep = isensor.sleep_state()
    #html = "<html><body>It is now %s.</body></html>" % tem
    html = "<!DOCTYPE html><html><head><title>wifi_iot</title><style>body{text_align:center}</style></head><body><div><h1>栗润泽: 165120215 毕业设计--基于wifi的人睡眠监控系统 </h1></div> <p> data from isensor </p><p>views:%s</p><p>mpu6050:%s </p><p>max30100:%s </p><p>睡眠状态统计结果:%s</p></body></html>" % (tem,tes,tss,sleep) 
    return HttpResponse(html)

def login(request):
    return render(request, 'login.html', {'articles': 18})
 
def book(request):
    return HttpResponse("this is caoyin read pages")
 
 
def movie(request):
    return render(request, 'index.html', {'articles': 18})
 
 
def book_detail(request, book_id, catgray):
    text = '文章详情页,该文章ID是：%s，分类是：%s' % (book_id, catgray)
    return HttpResponse(text)
