from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('Hello, you are on home page')
    return render(request,'index.html')

def about(request):
    return HttpResponse('Hello, you are on about page')


 