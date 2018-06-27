from flask import Flask, render_template, request, redirect, session, flash 
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"  

# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'Emails')

@app.route('/')
def index():
    # friends = mysql.query_db("SELECT * FROM friends")
    # print friends
    # return render_template('index.html', all_friends=friends)
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():

    import re
    # create a regular expression object that we can use run operations on
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    email = request.form['email']

    if len(email) < 1 or not EMAIL_REGEX.match(email):
        flash("Email is invalid!")     
        return redirect('/')
    else:

        query = "INSERT INTO Emails (Email_Addrs, created_on, updated_on) VALUES (:email, now(), now())"
        # Then define a dictionary with key that matches :variable_name in query.
    
        data = {'email': request.form['email'],}

        # Run query with inserted data.
        mysql.query_db(query, data)

        emails = mysql.query_db("SELECT * FROM Emails")
        #print emails 
        
        return render_template('success.html', all_emails=emails)
    
app.run(debug=True)