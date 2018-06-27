from flask import Flask, render_template, request, redirect, session, flash 

# import the Connector function
from mysqlconnection import MySQLConnector

#create Flask app
app = Flask(__name__)

# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')

# an example of running a query
#print mysql.query_db("SELECT * FROM friends")

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends;")
    print friends
    return render_template('index.html', all_friends=friends)

@app.route('/create', methods=['POST'])
def create():

    query = "INSERT INTO friends (first_name, last_name, age, created_at, updated_at, friend_since) VALUES (:first_name, :last_name, :age, now(), now(), now());"
    
    # Then define a dictionary with key that matches :variable_name in query.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'age': request.form['age']
           }

    # Run query with inserted data.
    mysql.query_db(query, data)

    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template undreturncopy redirect('/')
   
    return redirect('/')

app.run(debug=True)