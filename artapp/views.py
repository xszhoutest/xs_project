from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print(request.path,request.method)
    #请求头的元信息,GET请求参数*查询参数(
    print(request.META,request.GET)
    #POST请求(表单参数)
    print(request.POST)
    # return HttpResponse('<h1>你好<h1>')
    return render(request,'art/list.html',context={'name':'disen','age':20})