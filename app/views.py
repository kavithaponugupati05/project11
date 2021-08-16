from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'hello.html',context={'bookname':'python','authorname':'Guido van Rossum'})
