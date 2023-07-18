from flask import Flask

#print("INSIDE INIT FILE") #this can be used to debug

app = Flask(__name__)  # this is initializing the instance of the app
app.secret_key = 'Weights and Dates'