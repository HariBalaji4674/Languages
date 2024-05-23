from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'home.html',{'name' : 'Peddireddy','age' : '24'})

def calculator(request):
  return HttpResponse("Hello World Dear")