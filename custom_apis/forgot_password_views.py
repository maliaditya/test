from django.contrib import messages
from django.shortcuts import render,redirect
import datetime
from django.http import HttpResponse
# Create your views her
from authapp.models import  User
from requests.auth import HTTPBasicAuth
import requests
import json
from uuid import uuid4
from rest_framework.views import APIView

def enter_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        print(otp)
        phone = request.POST.get('phone')
        print(phone)
        data = {
            'otp':otp,
        }
        
        url = f'http://127.0.0.1:8000/api/user/{phone}/'
        response = requests.post(url, json=data)
        print(response.status_code)
        
        if response.status_code == 200:
            return redirect(f'http://127.0.0.1:8000/api/reset_password/{phone}')
        else:
            messages.error(request,'OTP not correct')
            return redirect(f'http://127.0.0.1:8000/api/{phone}')

    return render(request , 'custom_apis/enterotp.html')




def passreset(request, phone):
    if request.method == 'POST':
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        
        if re_password == password:
            u = User.objects.get(phone = phone)
            u.set_password(password)
            u.save()
            messages.success(request,'Password Successfully changed')
        else:
            messages.error(request,"Password do not match")

    return render(request , 'custom_apis/resetpassword.html')




