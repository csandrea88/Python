from flask import Flask, render_template, request, redirect, session, flash 

# import the Connector function
from mysqlconnection import MySQLConnector

#create a Flask app
app = Flask(__name__)

# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'Halodb')

# class Key(db.Model):
#     __tablename__ = 'keys'
#     id = db.Column('id', db.Integer, primary_key=True)
#     key = db.Column('key', db.Unicode)
#     value = db.Column('value', db.Unicode)

#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

@app.route('/')
def index():
    keys = mysql.query_db("SELECT * FROM Halodb.keys;")
    return render_template('index.html', all_keys=keys)
    # return render_template('index.html')

@app.route('/getv/<id>')
def getv(id):
    print "in getv route"
    print "id: ", id
#     keyRows = Key.query.all()
#     keys = mysql.query_db("SELECT key FROM Halodb.keys")
 
    keys = mysql.query_db("SELECT * FROM Halodb.keys;")
    
    val = ""
    for key in keys:
        if key['id'] == int(id):
            val = key['value']
    
    # query = "SELECT value FROM Halodb.keys WHERE key = :gKey"
    # data = {'gKey': gKey}
    # val = mysql.query_db(query, data).first()

    return render_template('index.html', value = val, all_keys=keys)
   
   #keyRows = Key.query.filter_by(key = gKey).first()
    #return keyRows.value
    # for kR in keyRows:   
    #     print kR.value


# @app.route('/setv') #needs key and value on this yet   
# def setv(sKey,sVal):
#    new_key = Key(sKey, sVal)
#    db.session.add(new_key)
#    db.session.commit()

# getVal = Get('cp2')
# print getVal

# setVal = Set('vac2','Hawaii')
# print setVal


app.run(debug=True)      