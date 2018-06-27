from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
#session['counter'] = 0 

@app.route('/') 
def home():
    
    session['counter'] += 1
    return render_template('index.html', counter = session['counter']) 
 
@app.route('/double', methods=['POST']) 
def double():
    session['counter'] += 2
    return render_template('index.html',counter = session['counter']) 

@app.route('/reset', methods=['POST']) 
def reset():
    session['counter'] = 0
    return render_template('index.html',counter = session['counter']) 
     
app.run(debug=True)

