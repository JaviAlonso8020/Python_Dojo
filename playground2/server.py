# from flask import Flask #this is the basic setup
# app = Flask(__name__)

from flask_app import app 
from flask_app.controllers import squares #replace rename_controller with your controller file name. Do not include .py

# we may need to add session secret key:
#app.secret_key = " my secret key"
# this goes in " __init__.py "

if __name__=='__main__':
    app.run(debug=True, port=5001)