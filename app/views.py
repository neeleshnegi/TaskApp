from django.shortcuts import render
from django.http import HttpResponse



def hello(request):
    return render(request,'app/index.html')

def name(request,bd):
    return render(request,'app/name.html',{'bd' : bd.capitalize() })