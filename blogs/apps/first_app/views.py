from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
  return render(request, "first_app/index.html")

def create(request):
  if request.method == "POST":
    print("*"*50)
    print(request.POST)
    print(request.POST['name'])
    print(request.POST['desc'])
    request.session['name'] = "test"
    print("*"*50)
    print(request.session['name'])
    return redirect("/")
  else:
    return redirect("/")