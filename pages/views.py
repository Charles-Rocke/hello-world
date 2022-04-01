from django.http import HttpResponse
from django.shortcuts import render
# add in import
from django.http import HttpResponse
# Create your views here.
def homePageView(request):
    return HttpResponse("Hello World")