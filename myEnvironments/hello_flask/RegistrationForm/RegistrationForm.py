from flask import Flask, render_template, request, redirect, session, flash 
app = Flask(__name__) 
app.secret_key = "ThisIsSecret!"  

@app.route('/') 
def process_form():
   return render_template('index.html') 
 
@app.route('/process', methods=['POST'])
def process():

    import re
    # create a regular expression object that we can use run operations on
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    success = "true"

    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    cpassword = request.form['cpassword']
    #print "here is the form data: {}".format(name)
    print fname.isalpha()
   
   #Validationss
    if len(fname) < 1 or not fname.isalpha():
         flash("First Name cannot be blank and must be a string")
         success = "false"
    
    if len(lname) < 1 or not lname.isalpha():
        flash("Last Name cannot be blank and must be a string!")
        success = "false"
    
    if len(email) < 1 or not EMAIL_REGEX.match(email):
        flash("Email cannot be blank and must be a valid email!")
        success = "false"
    
    if len(password) < 1 or len(password) > 8:
        flash("Password cannot be blank nor longer than 8 characters!")
        success = "false"

    if len(cpassword) < 1 or cpassword != password:
        flash("Confim password cannot be blank and it must match Password!")
        success = "false"
    
    if success == "false":
        return redirect('/')
    else:
        return render_template('process.html') 
   
app.run(debug=True)

