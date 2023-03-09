from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def chocolate(request):
    return HttpResponse('kitkat is the best chocolate')

def dark(request):
    return HttpResponse('dark chocolate is worst')
