from django.shortcuts import render

# Create your views here.

def home(request):
      return render(request,'calculator.html')

def result(request):
      a=request.GET.get('first')
      b=request.GET.get('second')
      c=int(a)+int(b)
      return render(request,'result.html',{'r':c})