from flask import Flask, render_template, request, redirect 
app = Flask(__name__)   

@app.route('/') 
def process_form():
   return render_template('index.html') 
   

# @app.route('/ninjas')
# def ninjas():
#   return render_template('ninjas.html')

# @app.route('/dojos')
# def dojos():
#   return render_template('dojos.html') 

@app.route('/process', methods=['POST'])
def process():

   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   #email = request.form['email']
   print "here is the form data: {}".format(name)

   # redirects back to the '/' route
   return render_template('index.html', prtname=name) 
   return redirect('/')
app.run(debug=True)

