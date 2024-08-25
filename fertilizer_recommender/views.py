from django.http import HttpResponse
from django.shortcuts import render




def fertilizer_recommend(request):
    return render(request, "fertRecommend.html")