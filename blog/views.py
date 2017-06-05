from django.shortcuts import render,HttpResponse
from datetime import date
from blog import models
ctime = date.today()

# Create your views here.



def index(request):
    return render(request,'index.html',{'title':'博客首页',
                                        'welcome':'欢迎来到我的博客',
                                        'ctime':ctime})
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        obj = models.User.objects.all()

        print(obj)
        return  render(request,'index.html',{'obj':obj})

def register(request):
    if request.method == 'GET':
        return render(request,'register.html',{'title':'注册'})
    elif request.method == 'POST':
        