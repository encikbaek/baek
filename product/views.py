from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    render(request, 'product/products.html')

def product(request):
    render(request, 'product/product.html')

def search(request):
    render(request, 'product/search.html')