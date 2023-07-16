from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja_model import Ninja 
from flask_app.models.dojo_model import Dojo 

    #importing the class here
    #There will be other imports need depending.... 
    # what you're trying to use in this file
    #You will also need a bycrypt... 
    # import (we will introduce this week 5)


@app.route('/create/ninja', methods=['POST']) #Post request route
def create_ninja():
    ninja_id = Ninja.save(request.form)
    print('@@@ we are here')
    dojo_id = Ninja.get_ninja_dojo(ninja_id)
    print(dojo_id)
    return redirect(f'/dojo/show/{dojo_id}')

# @app.route('/dojo/show/<int:dojo_id>') 
# def dojo_show(dojo_id):
#     return render_template("dojo_show.html", dojo = Dojo.get_dojo_with_ninjas(dojo_id))

@app.route('/ninjas') #Get request for 127.0.0.1:5000
def home():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', all_dojos = dojos)




@app.route('/dashboard')
def rename2():
    return render_template('Dashboard html page here!')