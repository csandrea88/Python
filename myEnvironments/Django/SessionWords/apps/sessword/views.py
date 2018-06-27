
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'sessword/index.html')

def process(request):
    if 'wlist' not in request.session:
        request.session['wlist']=[]
    wlist = request.session['wlist']
    
    print "The input word is: {}".format(request.POST['word'])
  
    word = request.POST['word']
    color = request.POST['color']

    #if request.POST['large'] == True:
    if 'large' in request.POST:
        large = "large"
    else:
         large = ""
    print "large is: {}".format(large)
    wlist += [[word,color,large]]
    request.session['wlist'] = wlist

    return redirect ("/")

def clear(request):    
    del request.session['wlist']
    
    return redirect ("/")
