from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
  context ={
    "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  print(context)
  return render(request, "first_app/index.html", context)