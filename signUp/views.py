from django.shortcuts import render , HttpResponse
#from .models import User,UserManager
from django.contrib.auth.models import User
from django import forms
from django.template.loader import render_to_string
from dict.models import Word

ch=False
def signUp(request):
    if request.method=="POST":
        global ch
        if 'IDcheck' in request.POST:
            username=request.POST['PID']
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('아이디가 이미 사용중입니다')
            elif username is '':
                raise forms.ValidationError('아이디를 입력해주세요')
            else:
                ch=True
                context={'PID':username,'check_available':True,'ID':True}
                return render(request,'signUp.html',context)
            return render(request, 'signUp.html')
        if 'submit' in request.POST:
            if ch ==True:
                username=request.POST['PID']
                password = request.POST['PPW']
                email=request.POST['PMail']

                if request.POST['PPW'] == request.POST['RPW']:
                    if username is '':
                        raise forms.ValidationError('아이디를 입력해주세요')
                    elif request.POST['PPW'] is not None :
                        User.objects.create_user(
                            username,password,email
                        )
                        return render(request,'home.html')
                    return render(request,'signUp.html')
                else:
                    forms.ValidationError('비밀번호가 일치하지 않습니다')
            else:
                raise forms.ValidationError('아이디 중복확인을 해주세요')
        return render(request,'signUp.html')
    return render(request,'signUp.html')
