from flask import Flask, render_template, request, redirect, session, flash 
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')
app.secret_key = "ThisIsSecret!"  

import md5 
import os, binascii # include this at the top of your file
import re

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/register')
def showsucess():
    return render_template ('Success.html')

@app.route('/login', methods=['POST'])
def login():
   
    userid = request.form['userid']
    password = request.form['password']
     
    query = "SELECT * FROM users WHERE userid = :userid"
    data = {'userid': userid}
    user = mysql.query_db(query, data)

    
    if len(user) > 0:
        session['fname'] = user[0]['first_name']
        session['lname'] = user[0]['last_name']
        session['userid'] = user[0]['userid']
        session ['success_message'] = "You are logged in"

        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()

        if user[0]['password'] == encrypted_password:
            #session['userid'] = request.form['userid']
            return render_template ('Success.html')
        else:
            flash("Incorrect userid or password, please try again")
            return redirect('/')
    else:
        return render_template ('Registration.html')
        
     

@app.route('/register', methods=['POST'])
def register():
    
    
    # create a regular expression object that we can use run operations on
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    success = "true"

    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    userid = request.form['userid']
    password = request.form['password']
    cpassword = request.form['cpassword']
    
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['userid'] = request.form['userid']
    session ['success_message'] = "You are registered"

  
    
    #Check for duplicates
    query = "SELECT * FROM users WHERE userid = :userid"
    data = {'userid': userid}
    user = mysql.query_db(query, data)

    if len(user) > 0:
         flash("This userid already exists, please use a different userid")
         success = "false"

    if len(fname) < 1 or not fname.isalpha():
         flash("First Name cannot be blank and must be a string")
         success = "false"
    
    if len(lname) < 1 or not lname.isalpha():
        flash("Last Name cannot be blank and must be a string!")
        success = "false"
    
    if len(email) < 1 or not EMAIL_REGEX.match(email):
        flash("Email cannot be blank and must be a valid email!")
        success = "false"
    
    if len(userid) < 1:
        flash("Userid cannot be blank!")
        success = "false"

    if len(password) < 1 or len(password) > 8:
        flash("Password cannot be blank nor longer than 8 characters!")
        success = "false"

    if len(cpassword) < 1 or cpassword != password:
        flash("Confim password cannot be blank and it must match Password!")
        success = "false"
    
    if success == "false":
        return render_template('Registration.html')
    else:
        salt =  binascii.b2a_hex(os.urandom(15))
        hashed_pw = md5.new(password + salt).hexdigest()

        query = "INSERT INTO USERS (first_name, last_name, email, userid, password, salt,updated_on, created_on) VALUES (:fname, :lname, :email, :userid, :password, :salt, now(), now())"
    
        data = {
            'fname': fname,
            'lname': lname,
            'email': email,
            'userid': userid,
            'password': hashed_pw,
            'salt': salt
        }

        # Run query with inserted data.
        user = mysql.query_db(query, data)

        if user > 0:
            return redirect('/register')
        else: 
            flash("Your registration was unsuccessful, please try again")
            return render_template ('Registration.html')

app.run(debug=True)
