from kat.views import *
from django.urls import path 
app_name='something'
urlpatterns=[
    path('chocolate/',chocolate,name='chocolate'),
    path('dark/',dark,name='dark')
]