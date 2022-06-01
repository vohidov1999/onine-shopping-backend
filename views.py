from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def asosiy(request):
    return render(request=request, template_name='home.html')

def login(request):
    return render(request=request, template_name='login.html')

def ulash(request):
    yangiliklar =News.objects.all()
    return render(request=request,template_name='index.html',context={'news': yangiliklar})

def single(request,slug):
    try:
        yangilik =News.objects.get(slug=slug)
        return render(request=request,template_name='single.html',context={'yangilik':yangilik})
    except:
        return HttpResponse("<h1>Siz izlayotgan yangilik mavjud emas</h1>")
