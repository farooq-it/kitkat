from kit.views import *
from django.urls import path 
app_name='something'
urlpatterns=[
    path('dark/',dark,name='dark'),
    path('chocolate/',chocolate,name='chocolate'),
]