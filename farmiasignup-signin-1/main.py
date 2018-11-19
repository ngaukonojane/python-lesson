from flask import (Flask,
                   render_template,
                   redirect,
                   url_for,
                   request
                   
                   )
import models
from models import Farmer
app = Flask('app')


@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/farmersign', methods=['POST', 'GET'])
def add():
    data = dict(request.form.items())
    if data.get('username', None):
        Farmer.add(
          username =data.get('username','janelodipo'),       
      
           email =data.get('email','janelodipo@gmail.com'),      
           phone =data.get('phone',10),          
           
           
        )
        
    return render_template('farmers.html')
@app.route('/farmerlist')
def lists():
  models.initialize()
  farmers = Farmer.select()
  return render_template("farmer_list.html", farmers=farmers)

app.run(debug=True, host='0.0.0.0', port=8080)