from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User 
    #importing the class here
    #There will be other imports need depending.... 
    # what you're trying to use in this file
    #You will also need a bycrypt... 
    # import (we will introduce this week 5)


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users') #Get request for 127.0.0.1:5000
def users():
    users = User.get_all()
    print(users)
    return render_template('read_all.html', all_users = users)

@app.route('/user/new') #Post request route
def new():
    return render_template("create.html")

@app.route('/user/create', methods =['POST'])
def create():
    # data = {
    #     "first_name": request.form["first_name"],
    #     "last_name": request.form["last_name"],
    #     "email": request.form["email"]
    # }
    User.save(request.form)
    return redirect('/users')
    


@app.route('/dashboard')
def rename2():
    return render_template('Dashboard html page here!')