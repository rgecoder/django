from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
  if 'counter' not in request.session:
    request.session['counter'] = 1
  else:
    request.session['counter'] += 1

  context ={
    "random_string": get_random_string(length=14)
  }
  print (request.session['counter'])
  return render(request,'word/index.html',context)

def reset(request):
  request.session['counter'] = 0
  return redirect ('/')