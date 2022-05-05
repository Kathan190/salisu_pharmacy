from curses.ascii import HT
from django.http import HttpResponse, request
from django.shortcuts import render
 
# Create your views here.
def index(request):
    return render(request, 'pharmacy/index.html')