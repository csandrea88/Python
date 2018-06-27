from flask import Flask, render_template, request, redirect 
app = Flask(__name__)   

@app.route('/') 
def hello_world():
   return render_template('index.html') 

@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')

@app.route('/dojos')
def dojos():
  return render_template('dojos.html') 

# @app.route('/dojos', methods=['POST'])
# def new_user():
#    print "Got Post Info" 

#    # we'll talk about the following two lines after we learn a little more
#    # about forms
#    name = request.form['name']
#    email = request.form['email']

#    alert (name, email)

#    # redirects back to the '/' route
#    return redirect('/')
app.run(debug=True)

