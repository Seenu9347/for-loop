from django.shortcuts import render

# Create your views here.

def uday(request):
    d={'name':'friends'}
    return render(request,'uday.html',d)
