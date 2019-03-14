# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
 
#计算相加页面跳转1
# def home(request):
#     return render(request, 'learn/home.html')
# def add2(requset):
#     a=requset.GET['a']
#     b=requset.GET['b']
#     print(a)
#     c=int(a)+int(b)
#     return HttpResponse(str(c))
# def add(requset,a,b):
#     c=int(a)+int(b)
#     return HttpResponse(str(c))

#模板继承
# def home(request):
#     # return render(request, 'base_模板继承.html')
#     return render(request, 'index_模板继承.html')

# 模板填充数据
# def home(request):
#     string="xiaokeji"
#     TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
#     dic={"key":"22","value":"33"}
#     return render(request, 'mobanjinjie.html', {'TutorialList': TutorialList,"string":string,"zidian":dic})

#数据库
# def home(request):
#     return render(request, 'base_模板继承.html')

#表单

def index(request):
    return render(request, '首页.html')
def add(requset):
    a=requset.POST['username']
    b=requset.POST['password']
    print(a)
    c=int(a)+int(b)
    return HttpResponse(str(c))

