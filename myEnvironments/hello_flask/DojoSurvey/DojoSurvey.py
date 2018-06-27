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
   dojoloc = request.form['dojoloc']
   favlang = request.form['favlang']
   comment = request.form['comment']
   #print "here is the form data: {}".format(name)

   # redirects back to the '/' route
   return render_template('process.html', prtname=name,prtdojoloc=dojoloc,prtfavlang=favlang,prtcomment=comment) 
   #return redirect('/')

@app.route('/index', methods=['POST']) 
def Go_Back():
   return redirect('/')

app.run(debug=True)

