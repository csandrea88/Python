from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 


@app.route('/') 
def home():

    session['totalgold'] = 0
    session['activities'] = []


    return render_template('index.html') 
 
@app.route('/process', methods=['POST']) 
def submit():
        import random 
        import datetime
        ts = datetime.datetime.fromtimestamp(1518377161).isoformat()
    
        if request.form['action'] == 'farm':
            farmgold = random.randrange(10, 21)
            session['totalgold'] += farmgold
            session['activities'].append("Earned {} golds from the farm({})".format(farmgold,ts))
        
        elif request.form['action'] == 'cave':
            cavegold = random.randrange(5, 11)
            session['totalgold'] += cavegold
            session['activities'].append("Earned {} golds from the cave({})".format(cavegold,ts))

        elif request.form['action'] == 'house':
            housegold = random.randrange(2,6)
            session['totalgold'] += housegold
            session['activities'].append("Earned {} golds from the house({})".format(housegold,ts))

        elif request.form['action'] == 'casino':
            casinogold = random.randrange(-50,50)
            session['totalgold'] += casinogold

            if casinogold >= 0:
                session['activities'].append("Earned {} golds from the casino({})".format(casinogold,ts))
            else:
                session['activities'].append("Entred a casino and lost {} golds. Ouch... ({})".format(casinogold,ts))
        
        return render_template('index.html', totgold=session['totalgold'], activities=session['activities']) 

app.run(debug=True)

