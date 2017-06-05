from django.shortcuts import render,HttpResponse,redirect
from datetime import date
from blog import models
ctime = date.today()
from django import forms
# Create your views here.

class FM(forms.Form):
    name = forms.CharField(error_messages={'required':'用户名不能为空','invalid':'用户命格式错误'})
    cname = forms.CharField(required=False)
    pwd = forms.CharField(max_length=16,
                          min_length=6,
                          error_messages={'required':'密码名不能为空',
                                          'max_length':'密码太长',
                                          'min_length':'密码太短'})


def index(request):
    return render(request,'index.html',{'title':'博客首页',
                                        'welcome':'欢迎来到我的博客',
                                        'ctime':ctime})
def login(request):
    if request.method == 'GET':
        return render(request,'login.html',{'title':'登录'})
    elif request.method == 'POST':
        fm = FM(request.POST)
        r1 = fm.is_valid()
        print(r1)
        if r1:
            name = request.POST.get('name')
            pwd = request.POST.get('pwd')
            obj = models.User.objects.all().filter(name=name,pwd=pwd).first()
            if obj:
                return render(request,'index.html',{'obj':obj,'title':'首页'})
            else:
                return render(request,'login.html')
        else:
            print(fm.errors)
            return render(request,'login.html',{'obj':fm,'title':'登录'})

def register(request):
    if request.method == 'GET':
        return render(request,'register.html',{'title':'注册'})
    elif request.method == 'POST':
        obj = FM(request.POST)
        r1 = obj.is_valid()
        if r1:
            print(obj.cleaned_data)
            models.User.objects.create(**obj.cleaned_data)
            return redirect(to='login.html')
        else:
            print(obj.errors)
            return render(request,'register.html',{'obj':obj,'title':'注册'})

