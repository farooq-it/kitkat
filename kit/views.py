from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dark(request):
    return HttpResponse('dark chocolate is the tastiest')

def chocolate(request):
    return HttpResponse('kitkat is the worst chocolate')