from django.shortcuts import render

# Create your views here.
def data_render(request):
    d = {'Name':'Soumya','age':26}
    return render(request,'data_render.html',context=d)

def if_else(request):
    d = {'a':12,'b':15}
    return render(request,'if_else.html',context=d)

def if_elif_else(request):
    d = {'a':10,'b':30,'c':25}
    return render(request,'if-elif-else.html',context=d)

def nested_if(request):
    d = {'a':20,'b':30,'c':40}
    return render(request,'nested_if.html',context=d)



