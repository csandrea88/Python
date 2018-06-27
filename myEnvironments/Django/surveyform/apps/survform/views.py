from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
#from time import gmtime, strftime
 
def index((request)):
   return render(request,'survform/index.html')

def result((request)):
   return render(request,'survform/process.html')

def process(request): 
    if not 'name' in request.session:
        request.session['name'] = ""
    if not 'dojoloc' in request.session:
        request.session['dojoloc'] = ""
    if not 'favlang' in request.session:
        request.session['favlang'] = ""
    if not 'comment' in request.session:
        request.session['comment'] = ""
    if not 'counter' in request.session:
        request.session['counter'] = 0

    request.session['counter'] += 1
    print request.session['counter'], request.POST['name']
    request.session['name'] = request.POST['name']
    request.session['dojoloc'] = request.POST['dojoloc']
    request.session['favlang'] = request.POST['favlang']
    request.session['comment'] = request.POST['comment']

    return redirect ('/survform/result')

def goback(request): 
    
    return redirect ('/')

# def index(request):  #initial or reset request
#     if not 'counter' in request.session:
#         request.session['counter'] = 0
#     request.session['counter'] += 1
#     context = {
#         "randstr": get_random_string(length=14)
#     }
#     return render(request,'randword/index.html', context)


# def reset(request):   #with method=POST?
#     if 'counter' in request.session:
#         del request.session['counter']

#     return redirect ("/")
  
