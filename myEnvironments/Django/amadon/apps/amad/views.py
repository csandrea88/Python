from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'amad/index.html')

def checkout(request):
    return render(request,'amad/process.html')

def process(request):

    if 'acumtot' not in request.session:
        request.session['acumtot']=0
    if 'acumqty' not in request.session:
        request.session['acumqty']=0
    
    request.session['currspend'] = 0

    arr = [14.99,29.99,9.50]

    qty = int(request.POST['qty'])
    prodnum = int(request.POST['prodnum'])

    request.session['currspend'] = qty * arr[prodnum]
    request.session['acumtot'] += request.session['currspend']
    request.session['acumqty'] += qty

    return redirect ("/amad/checkout")

def goback(request):    
    
    return redirect ("/")