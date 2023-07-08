from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.rename_model import Rename #importing the class here
#There will be other imports need depending what you're trying to use in this file
#You will also need a bycrypt import (we will introduce this week 5)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST']) #Post request route
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('/result.html')