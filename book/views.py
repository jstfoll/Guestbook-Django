from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'book/index.html')

def sign(request):
    return render(request,'book/sign.html')
    