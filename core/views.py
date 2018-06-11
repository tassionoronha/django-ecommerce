# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req, 'index.html')

def contact(req):
    return render(req, 'contact.html')

def product(req):
    return render(req, 'product.html')

def product_list(req):
    return render(req, 'product_list.html')
