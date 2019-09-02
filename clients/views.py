from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'clients/profiles.html')

def creates(request):
    return render(request, 'clients/creates.html')

def access(request):
    return render(request, 'clients/access.html')