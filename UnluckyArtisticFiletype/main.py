from flask import Flask
from flask import render_template
from flask import request


app = Flask('app')
@app.route("/")
def index():  
    return render_template('index.html')

@app.route('/multiply', methods= ['POST'])
def results():
  data = dict(request.form.items())
  val1 = int(data.get('val1',0))
  val2 = int(data.get('val2',0))
  
  product = val1*val2
  context = {'product':product, 'val1':val1,'val2':val2}
      
  return render_template("result.html",**context)
app.run(debug=True, host='0.0.0.0',port=8080) 
 
   