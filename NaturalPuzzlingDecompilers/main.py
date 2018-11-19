from flask import (Flask, render_template, request, make_response)
import json

app = Flask('app')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/welcome', methods=['POST'])
def welcome():
    data = dict(request.form.items())
    name = str(data.get('name', 'Guest'))
    email = str(data.get('email', 'no@email.com'))
    course = str(data.get('course', 'Not provided'))
    context = {'name':name, 'email':email, 'course': course}
    response = make_response(render_template("welcome.html", **context))
    response.set_cookie('register_app',json.dumps(context))
    return response

@app.route('/edit')
def edit():
    data = request.cookies.get('register_app')
    context = json.loads(data)
    response = make_response(render_template("edit.html", **context))
    return response



app.run(debug=True, host='0.0.0.0', port=8080)