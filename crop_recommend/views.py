from django.http import HttpResponse
from django.shortcuts import render




def crop_recommend(request):
       
        return render(request,"cropRecommender.html")

