from django.shortcuts import render,redirect,HttpResponse
from time import strftime, localtime

# Create your views here.
def index(request):
  return render(request, "word/index.html")

def add_word(request):
  if request.method == "POST":
    wordtime = strftime('%H:%M:%S:%p, %B %d %Y',localtime())
    if 'words' not in request.session:
      request.session['words'] = []
    if 'big_font' in request.POST:
      showbig = 'big'
    else:
      showbig = 'small'
    
    data = {'word': request.POST['word'],
            'color':request.POST['color'],
            'font': showbig,
            'time': wordtime}
    
    # request.session['words'].append(data)
    # print (request.session['words'])
    
    # appending directly will not work
    #Django does not allow to use .append() on list in session

    temp_list = request.session['words']
    temp_list.append(data)
    request.session['words'] = temp_list

    return redirect ('/')
  else:
    return redirect ('/')

def clear(request):
  request.session.clear()
  return redirect ('/')

    
    
    
    
