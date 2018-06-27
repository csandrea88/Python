from django.shortcuts import render, redirect

def index(request):
    return render(request,'ninjgold/index.html')# Create your views here.

def process(request):

        import random 
        import datetime
        ts = datetime.datetime.fromtimestamp(1518377161).isoformat()
        
        if 'totalgold' not in request.session:
            request.session['totalgold']=0
        if 'activities' not in request.session:
            request.session['activities']=[]
        

        if request.POST['action'] == 'farm':
            farmgold = random.randrange(10, 21)
            request.session['totalgold'] += farmgold
            request.session['activities'].append("Earned {} golds from the farm({})".format(farmgold,ts))
        
        elif request.POST['action'] == 'cave':
            cavegold = random.randrange(5, 11)
            request.session['totalgold'] += cavegold
            request.session['activities'].append("Earned {} golds from the cave({})".format(cavegold,ts))

        elif request.POST['action'] == 'house':
            housegold = random.randrange(2,6)
            request.session['totalgold'] += housegold
            request.session['activities'].append("Earned {} golds from the house({})".format(housegold,ts))

        elif request.POST['action'] == 'casino':
            casinogold = random.randrange(-50,50)
            request.session['totalgold'] += casinogold
            
            if casinogold >= 0:
                request.session['activities'].append("Earned {} golds from the casino({})".format(casinogold,ts))
            else:
                request.session['activities'].append("Entred a casino and lost {} golds. Ouch... ({})".format(casinogold,ts))
       
        
        return redirect("/")