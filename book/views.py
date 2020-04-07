from django.shortcuts import render,redirect
from .models import comment
from .forms import commentform
# Create your views here.

def home(request):
    com = comment.objects.order_by('-id')
    context={'comment' : com }
    return render(request,'book/index.html', context)

def sign(request):
    if request.method == 'POST':
        form=commentform(request.POST)

        if form.is_valid():
            new_comment= (comment(name=request.POST['name'],comment=request.POST['comment'])).save()  # from the models.py section
            return redirect('home')
    else:
        form=commentform()
    context={'form' : form }

    return render(request,'book/sign.html' , context)
    