from django.shortcuts import render
from urllib import request


# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def mens(request):
    context = {}
    return render(request, 'mens.html', context)    

def womens(request):
    context = {}
    return render(request, 'womens.html', context)    

def sale(request):
    context = {}
    return render(request, 'sale.html', context) 

def men1(request):
    context = {}
    return render(request, 'men1.html', context) 

def men2(request):
    context = {}
    return render(request, 'mens2.html', context) 

def women1(request):
    context = {}
    return render(request, 'womens1.html', context) 

def sale1(request):
    context = {}
    return render(request, 'sales1.html', context) 

def sale2(request):
    context = {}
    return render(request, 'sales2.html', context) 