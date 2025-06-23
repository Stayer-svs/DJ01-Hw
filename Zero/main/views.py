from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html',{'caption':"DjangoClock"})


def new(request):
    return render(request, 'main/new.html')


def doc(request):
    return render(request, 'main/doc.html')
    #return HttpResponse("<h1>Это 3-я страница моего проекта на Django</h1>")

def adr(request):
    return render(request, 'main/adr.html')
    #return HttpResponse("<h1>Это 4-я страница моего проекта на Django</h1>")
