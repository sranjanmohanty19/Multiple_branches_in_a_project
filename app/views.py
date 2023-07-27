from django.shortcuts import render

# Create your views here.
def data_render(request):
    d = {'Name':'Soumya','age':26}

    return render(request,'data_render.html',context=d)