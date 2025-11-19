from django.http import HttpResponse
from django.shortcuts import render

#class based view


#function based view

# def home(request):
#     return HttpResponse("welcome to Django")
#
# def index(request):
#     return HttpResponse('index page')
# def new(request):
#     return HttpResponse('WELCOME TO NEW PAGE')


def home(request):
    context={'name':'arun','age':'28'}
    return render(request,'home.html',context)

def index(request):
    return render(request,'index.html')