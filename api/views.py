from django.shortcuts import render
from api.models import *
from django.http import HttpResponseRedirect, HttpResponse

from rest_framework.views import APIView

import json
# Create your views here.

class LoginView(APIView):
    def post(self,request):
        name=request.POST.get('name')
        email=request.POST.get('email')
        u=UserLogin.objects.filter(email=email)
        print name
        if len(u)==0:
            u=UserLogin(username=name,email=email)
            u.save()
        return HttpResponse(json.dumps({"res:":1}))

class GCMView(APIView):
    def post(self,request):
        email=request.POST.get('email')
        key=request.POST.get('key')
        u=UserLogin.objects.get(email=email)
        u.gcm=key
        u.save()
        return HttpResponse(json.dumps({"res":1}))
