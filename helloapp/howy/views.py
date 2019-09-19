
from distutils.command import register
 
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context) 

def login(request):
    return render(request, 'login.html', {'articles': 18})
 
def book(request):
    return HttpResponse("this is caoyin read pages")
 
 
def movie(request):
    return render(request, 'index.html', {'articles': 18})
 
 
def book_detail(request, book_id, catgray):
    text = '文章详情页,该文章ID是：%s，分类是：%s' % (book_id, catgray)
    return HttpResponse(text)
