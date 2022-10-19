import http
from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from cmsapp.models import regform
from datetime import datetime


def form(request):
    if request.method=='POST':
        # Question =request.POST['q']
        answer =request.POST['a']
        user= regform.objects.create(answer=answer)
        user.save()
        return render(request, 'core/done.html')
    else:
        return render(request, 'core/base.html')

def done(request):
    return render(request, 'core/done.html')