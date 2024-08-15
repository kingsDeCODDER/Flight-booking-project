from django.shortcuts import render

def myfunction(request):
    return render(request,'index.html')
