import imp
from django.urls import path
from .views import *

urlpatterns =[
    path('', form , name= 'form'),
    path('done',done, name='done')
]
