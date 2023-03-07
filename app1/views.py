from django.shortcuts import render

# create your views here
from django.http import HttpResponse


def hari (request):
    return HttpResponse('<h1>welcome to django<h1>')

def harish(request):
    return HttpResponse('<marquee><h1>jango project</h1>')

