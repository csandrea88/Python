from flask import Flask, render_template, request, redirect, session, flash 

# import the Connector function
from mysqlconnection import MySQLConnector

#create a Flask app
app = Flask(__name__)

#secret key for flash error messaging
app.secret_key = 'KeepItSecretKeepItSafe'


# connect and store the connection in "mysql"; note that you pass the database name to the function

mysql = MySQLConnector(app, 'Halodb')

# This is how a model can be used in python/flask, but I chose to use 
# mysql workbench and a re-usable mysqlconnection.py component.
# The current setup with a Connection component allows me to be able to create very readable & re-usuable SQL statements
#
# class Key(db.Model):
#     __tablename__ = 'keys'
#     id = db.Column('id', db.Integer, primary_key=True)
#     key = db.Column('key', db.Unicode)
#     value = db.Column('value', db.Unicode)

    # def __init__(self, key, value):
    #     self.key = key
    #     self.value = value

@app.route('/')
def LoginReg():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def Register():
        
    errmessage = False

    if len(request.form['name']) < 1: 
        flash("Registration: Name cannot be blank")
        errmessage = True
    if len(request.form['userid']) < 1:
        flash("Registration: Userid cannot be blank")
        errmessage = True
    if len(request.form['password']) < 1:
        flash("Registration: Password cannot be blank")
        errmessage = True
    
    if errmessage == False:
        
        gname = request.form['name']
        guserid = request.form['userid']
        gpassword = request.form['password']

        query = """SELECT * FROM Halodb.users WHERE Halodb.users.userid = '%s';""" % (guserid)
        
        data = {'guserid': guserid}
        val = mysql.query_db(query, data)

        if len(val) >= 1: 
            flash("This userid already exists, please try again")
            return redirect('/')
        else: 
            query = """INSERT INTO Halodb.users(Halodb.users.name, Halodb.users.userid, Halodb.users.password) VALUES ('%s', '%s', '%s');""" % (gname, guserid, gpassword)
            print "Insert Query: ", query
            data = {'gname': gname, 'guserid': guserid, 'gpassword': gpassword}
            InsRow = mysql.query_db(query, data)
            print "InsRow:  ", InsRow
            session['name'] = gname
            session['UID'] = InsRow
            print "InsRow:  ", InsRow, session['name'], session['UID']
            return redirect('/getset')
    else:
        return redirect('/') 
            
@app.route('/login', methods=['POST'])
def Login():

        errmessage = False

        guserid = request.form['userid']
        gpassword = request.form['password']


        if len(guserid) < 1:
            flash("Login: Userid cannot be blank")
            errmessage = True
        if len(gpassword) < 1:
            flash("Login: Password cannot be blank")
            errmessage = True
        
        if errmessage == False:

            query = """SELECT * FROM Halodb.users WHERE Halodb.users.userid = '%s' and Halodb.users.password = '%s';""" % (guserid, gpassword)
            data = {'guserid': guserid, 'gpassword': gpassword}
            val = mysql.query_db(query, data)
            print "query: ", query
            print "Val:  ", val
    
            if len(val) > 0:
                session['UID'] = val[0]['id']
                session['name'] = val[0]['name']
                return redirect('/getset')
            else:
                flash("Login information incorrect")
                return redirect('/') 

        else:
            return redirect('/')

@app.route('/getset')
def getset():
    print "in /getset"
    
    # return 'You are logged in'
    SessUID = session['UID']
    query = """SELECT * FROM Halodb.keys WHERE Halodb.keys.userid  = '%s' ORDER BY Halodb.keys.key ASC;""" % (SessUID)
    print "query:  ", query
    data = {'SessUID': SessUID}
    keys = mysql.query_db(query, data)

    return render_template('getset.html', all_keys=keys, okey="", ovalue="")
    # keys = mysql.query_db("SELECT * FROM Halodb.keys WHERE Halodb.keys.userid = '%s ' ORDER BY Halodb.keys.key ASC; % (Val3)")
    # return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    
    errmessage = False
    gKey = request.form['key']
    gVal = request.form['value']
    SessUID = session['UID']
    val = ""

    if request.form['action'] == 'Get':

        if len(gKey) < 1: 
            flash("Get: Key cannot be blank")
            errmessage = True

        if errmessage == False:
        
            query = """SELECT * FROM Halodb.keys WHERE Halodb.keys.userid  = '%s' ORDER BY Halodb.keys.key ASC;""" % (SessUID)
            print "query:  ", query
            data = {'SessUID': SessUID}
            keys = mysql.query_db(query, data)

            keyNF = True

            for key in keys:
                if key['key'] == gKey:
                    keyNF = False
                    val = key['value']
                    print "val: ", val

            if keyNF == True:
                flash("Get: Key doesn't exist")
        
            return render_template('getset.html', all_keys=keys, okey= gKey, ovalue = val)
        
        else:

            return redirect('/getset')

    else:

        if len(gKey) < 1: 
            flash("Get: Key cannot be blank")
            errmessage = True
        if len(gVal) < 1: 
            flash("Get: Value cannot be blank")
            errmessage = True

        if errmessage == False:
            print "in setv"
            print gKey

            #Search database to see if key exists already
            query = """SELECT value FROM Halodb.keys WHERE Halodb.keys.key = '%s' and Halodb.keys.userid = '%s';""" % (gKey, SessUID)
            print "query:  ", query
            data = {'gKey': gKey}
            val = mysql.query_db(query, data)
            print "len of array val: ", len(val)

            #if a row was returned then update the value from the form
            if len(val) > 0:
                print "value:  ", val[0]['value']
                query = """UPDATE Halodb.keys SET Halodb.keys.value = '%s' WHERE Halodb.keys.key = '%s';""" % (gVal, gKey)
                print "Update Query: ", query
                data = {'gKey': gKey, 'val':val}
                mysql.query_db(query, data)

            #if no rows exist with key then Insert the key/value pair
            else:
                SessUID = session['UID']
                query = """INSERT INTO Halodb.keys(Halodb.keys.key, Halodb.keys.value, Halodb.keys.userid) VALUES ('%s', '%s', '%s');""" % (gKey, gVal, SessUID)
                print "Insert Query: ", query
                data = {'gKey': gKey, 'val':val, 'SessUID': SessUID}
                InsRow = mysql.query_db(query, data)
                print "InsRow:  ", InsRow
          
            return redirect('/getset')
        
        else:
            
            query = """SELECT * FROM Halodb.keys WHERE Halodb.keys.userid  = '%s' ORDER BY Halodb.keys.key ASC;""" % (SessUID)
            data = {'SessUID': SessUID}
            keys = mysql.query_db(query, data)
            return render_template('getset.html', all_keys=keys, okey= gKey, ovalue = gVal)

        


@app.route('/logout')
def Logout():
    print "in logout route"
    session.clear()
    return redirect('/')

app.run(debug=True)      