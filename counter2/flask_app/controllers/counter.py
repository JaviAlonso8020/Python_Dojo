from flask_app import app
from flask import render_template, redirect, request, session, flash
# from flask_app.models.rename_model import Rename 
    #importing the class here
    #There will be other imports need depending.... 
    # what you're trying to use in this file
    #You will also need a bycrypt... 
    # import (we will introduce this week 5)


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] +=1
    return render_template('index.html')

@app.route('/add2')
def add2():
    session['count'] +=1
    return redirect('/')

@app.route('/destroy_session') 
def reset():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def rename2():
    return render_template('Dashboard html page here!')