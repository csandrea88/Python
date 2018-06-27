from flask import Flask, render_template, request, redirect, session, flash 
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')
# an example of running a query
#print mysql.query_db("SELECT * FROM friends")

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html', allfriends=friends)

app.run(debug=True)
