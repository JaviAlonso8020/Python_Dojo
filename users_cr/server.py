from flask import Flask, render_template, request, redirect

from users import User

app = Flask(__name__)

from flask_app import app 
# from flask_app.controllers import rename_controller #replace rename_controller with your controller file name. Do not include .py

# we may need to add session secret key:
#app.secret_key = " my secret key"
# this goes in " __init__.py "

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods =['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

if __name__=='__main__':
    app.run(debug=True, port=5001)