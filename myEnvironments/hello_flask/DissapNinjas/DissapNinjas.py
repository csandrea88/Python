from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/') 
def Home():
   return render_template('index.html') 
 
@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')

@app.route('/ninja/<color>')
def ninja(color):
    if color == "blue":
        return render_template('ninjablue.html')
    elif color == "orange":
       return render_template('ninjaorange.html')
    elif color == "red":
        return render_template('ninjared.html')
    elif color == "purple":   
        return render_template('ninjapurple.html')
    else:
        return render_template('index.html')

app.run(debug=True)

