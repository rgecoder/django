from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

# Create your views here.
def index(request):
  if 'total_gold' not in request.session or 'activities' not in request.session:
    request.session['total_gold'] = 0
    request.session['activities'] =[]
  return render(request,'home/index.html')

def process_money(request):
  if request.method=='POST':
    if request.POST['building'] == 'farm':
      gold = random.randint(10,20)
      request.session['activities'].append('You earned ' + str(gold) + ' gold from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M"))+ ')')
    elif request.POST['building'] == 'cave':
      gold = random.randint(5,10)
      request.session['activities'].append('You earned ' + str(gold) + ' gold from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M"))+ ')')
    elif request.POST['building'] == 'house':
      gold = random.randint(2,5)
      request.session['activities'].append('You earned ' + str(gold) + ' gold from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M"))+ ')')
    if request.POST['building'] == 'casino':
      gold = random.randint(-50,50)
      request.session['activities'].append('You earned ' + str(gold) + ' gold from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M"))+ ')')
    
    request.session['total_gold'] += gold

  return redirect('/')

def reset(request):
  if request.method == "POST":
    request.session.clear()
  
  return redirect('/')