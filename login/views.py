from django.shortcuts import render , HttpResponse,redirect
#from dictionary.models import User,UserManager
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms

def login(request):
    if request.method == "POST":
        SID=request.POST['SID']
        SPW = request.POST['SPW']

        user=authenticate(request,username=SID,password=SPW)
        if user is not None:
            return redirect('http://127.0.0.1:8000/')
        else:
            raise forms.ValidationError('아이디나 비밀번호가 잘못 입력되었습니다.')
        return render(request,'login.html')

    return render(request,'login.html')
        