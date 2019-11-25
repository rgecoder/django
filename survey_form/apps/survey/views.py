from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
  return render(request, "survey/index.html")

def process(request):
  if request.method == "POST":
    
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']

    return redirect('/results')
  else:
    return redirect('/')

def results_page(request):

  return render(request, 'survey/results.html')

  