from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 


@app.route('/') 
def home():

    session['dcntr'] = 0
    print "root: {}".format(session['dcntr'])
    return render_template('index.html') 
 
@app.route('/process', methods=['POST']) 
def process():
    if request.form['submit'] == 'no':
        print "submit == no"
        #return render_template('NoSchool.html')
    else:
        print "submit == yes"
        return render_template('Dead.html')
            
@app.route('/Dead', methods=['POST']) 
def dead():
 
    session['dcntr'] += 1
    print "dead:{}".format(session['dcntr'])
    return render_template('index.html')

            
app.run(debug=True)

