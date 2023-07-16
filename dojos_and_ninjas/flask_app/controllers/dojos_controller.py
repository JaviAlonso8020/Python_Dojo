from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo_model import Dojo 
    #importing the class here
    #There will be other imports need depending.... 
    # what you're trying to use in this file
    #You will also need a bycrypt... 
    # import (we will introduce this week 5)


@app.route('/') #Get request for 127.0.0.1:5000
def index():
    return redirect ('/dojos')

@app.route('/dojo/create', methods=['POST'])
def dojo_create():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos')
def all_dojos():
    dojos = Dojo.get_all()   
    return render_template('dojos.html', all_dojos = dojos)


@app.route('/dojo/show/<int:dojo_id>') 
def dojo_show(dojo_id):
    return render_template("dojo_show.html", dojo = Dojo.get_dojo_with_ninjas(dojo_id))