from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def weed_detection(request):
    return render(request,'weed_detection.html')