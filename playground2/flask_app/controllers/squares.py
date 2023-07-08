from flask_app import app
from flask import render_template, redirect, request, session, flash
# from flask_app.models.rename_model import Rename 
#importing the class here
#There will be other imports need depending 
# what you're trying to use in this file
#You will also need a bycrypt import (we will introduce this week 5)


@app.route('/play/') #Get request for 127.0.0.1:5000
def level1():
    return render_template('index.html', num = 3, color = "blue")

@app.route('/play/<int:num>')  #Post request route
def level2(num):
    return render_template('index.html', num = num , color = "blue")

@app.route('/play/<int:num>/<string:color>')
def level3(num, color):
    return render_template("index.html", num = num, color = color)

