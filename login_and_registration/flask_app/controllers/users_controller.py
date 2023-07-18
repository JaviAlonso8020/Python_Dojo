from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User 
    #importing the class here
    #There will be other imports need depending.... 
    # what you're trying to use in this file
    #You will also need a bycrypt import 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/') #Get request for 127.0.0.1:5000
def home():
    return render_template('login_n_reg.html')

@app.route('/register', methods=['POST']) #Post request route
def register():
    if not User.validate_user(request.form): #if returns false, double neg
                                            #makes a positive, we are looking
                                            #for false to run the if statement 
        return redirect('/') #redirects do not take htmls
    pw_hash = bcrypt.generate_password_hash(request.form['password']) #salts and hashes
    print(pw_hash)  
    data ={  #we reconstructed use data in order to pass the hashed password
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    id = User.save(data)
    print("this is id from register", id)
    session['user_id'] = id
    session['first_name'] = request.form['first_name']
    return redirect('/welcome/')

@app.route('/welcome/')
def welcome():
    if 'user_id' not in session:
        return redirect('/logout')
    # data = {
    #     'id' : session['user_id']
    # }
    return render_template('welcome.html')

@app.route('/login', methods = ['POST'])
def login():
    data = {
        'email' : request.form['email']
    }
    user_in_db = User.find_user(data)
    if not user_in_db:
        flash("Invalid email/password!")
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    # never render on a post!!!
    return redirect('/welcome')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')