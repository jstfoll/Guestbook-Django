from django.shortcuts import render
from .models import comment
# Create your views here.

def home(request):
    com = comment.objects.order_by('id')
    context={'comment' : com }
    return render(request,'book/index.html', context)

def sign(request):
    return render(request,'book/sign.html')
    