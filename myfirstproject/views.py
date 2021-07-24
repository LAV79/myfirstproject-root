from django.http import HttpResponse
from django.shortcuts import render

def about(rq):
	return HttpResponse('Это страница Лобзова Алексея')

def home(rq):
	return render(rq,'home.html',{'g':'Привет всем сюда входящим!'})	