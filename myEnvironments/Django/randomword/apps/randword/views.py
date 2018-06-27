#Use this code to make sure your project is setup correctly
#
# from django.shortcuts import render, HttpResponse, redirect
#  # the index function is called when root is visited
# def index(request):
#   response = "Hello, I am your first request!"
#   return HttpResponse(response)

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
#from time import gmtime, strftime


def index(request):  #initial or reset request
    if not 'counter' in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    context = {
        "randstr": get_random_string(length=14)
    }
    return render(request,'randword/index.html', context)

def generate(request):   #with method=POST?
    
    return redirect ("/")

def reset(request):   #with method=POST?
    if 'counter' in request.session:
        del request.session['counter']

    return redirect ("/")
  
