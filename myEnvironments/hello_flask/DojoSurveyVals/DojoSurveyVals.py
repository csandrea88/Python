from flask import Flask, render_template, request, redirect, session, flash 
app = Flask(__name__) 
app.secret_key = "ThisIsSecret!"  

@app.route('/') 
def process_form():
   return render_template('index.html') 
 


@app.route('/process', methods=['POST'])
def process():

    # we'll talk about the following two lines after we learn a little more
    # about forms
    sucess = "true"
    name = request.form['name']
    dojoloc = request.form['dojoloc']
    favlang = request.form['favlang']
    comment = request.form['comment']
    #print "here is the form data: {}".format(name)

   #Validations
    if len(name) < 1:
        flash("Name cannot be blank!")
        sucess = "false"

    if len(comment) < 1 or len(comment) > 120:
        flash("Invalid comment length!")
        sucess = "false"
    
    if sucess == "false":
        return redirect('/')
    else:
        return render_template('process.html', prtname=name,prtdojoloc=dojoloc,prtfavlang=favlang,prtcomment=comment) 
   

@app.route('/index', methods=['POST']) 
def Go_Back():
   return redirect('/')

app.run(debug=True)

