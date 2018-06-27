from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 


@app.route('/') 
def home():
    import random       
    session['guess'] = random.randrange(0, 101)
    button_val="Submit"  
    print session['guess']
    session['button_val'] = "Submit"

    return render_template('index.html', gval="Submit") 
 
@app.route('/submit', methods=['POST']) 
def submit():

    if session['button_val'] == "Play Again?":
        print "redirecting"
        return redirect('/')
    else: 
        button_val = "Submit"
        guess = int(request.form['guess'])  
        sys_num = session['guess']

        if guess > sys_num:
            print "greater than; guess: {} and sys_num: {}".format(guess,sys_num)
            resp = "Too High, try again"
        elif guess < sys_num:
            print "less than; guess: {} and sys_num: {}".format(guess,sys_num)
            resp = "Too Low, try again"
        elif guess == sys_num:
            print "equal to; guess: {} and sys_num: {}".format(guess,sys_num)
            resp = "You win: the number is {}".format(sys_num)
            button_val="Play Again?"
            session['button_val'] = "Play Again?"
            
        
        #print "session guess: {}, user guess: {}, resp: {}, button_val: {}".format(sys_num, guess, resp, button_val)
        return render_template('index.html', gresp=resp, gval=button_val) 

app.run(debug=True)

