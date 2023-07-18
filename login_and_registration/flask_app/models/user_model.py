# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
#might need other imports like flash, other classes, regex
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

db = 'login_reg_schema'

# model the class after the friend table from our database
class User:
    def __init__(self, data):
        #follow database table fields plus any other attribute you want to create
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        print("@@@ we are saving")
        query = """INSERT INTO users (first_name, last_name,
                email, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s,
                %(password)s);
                """
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_user(user_form_data): # this is a dictionary
        is_valid = True
        if not (user_form_data['first_name']).isalpha():
            flash('First name must be A-Z only')
            is_valid = False
        if len(user_form_data['first_name']) < 2:
            flash('First name must be as least 2 characters')
            is_valid = False
        if not (user_form_data['last_name']).isalpha():
            flash('Last name must be A-Z only')
            is_valid = False
        if len(user_form_data['last_name']) < 2:
            flash('Last name must be as least 2 characters')
            is_valid = False
        if not EMAIL_REGEX.match(user_form_data['email']):
            flash("Invalid email/password address!")
            is_valid = False
        if len(user_form_data['password']) < 8:
            flash('Password needs at least 8 characters')
            is_valid = False
        if (user_form_data['password_confirmation']) != user_form_data['password']:
            is_valid = False
        return is_valid
    
    @classmethod
    def rename(cls):
        query = "SELECT * FROM users;"
                # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(db).query_db(query)
                #Nice little head start
        print(results)       
                #Rest of code here
                # Create an empty list to append our instances of friends
        # friends = []
                # Iterate over the db results and create instances of friends with cls.
        # for friend in results:
        #     friends.append(cls(friend))
        # return friends
        return "Something here"

    @classmethod
    def get_one(cls, user_id):
        query  = "SELECT * FROM friends WHERE id = %(id)s;"
        data = {'id': user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod  #if wanting to create an instance, we want to use a classmethod
    def find_user(cls, email_dict):
        query = """SELECT * FROM users
                WHERE email = %(email)s;
                """
        results = connectToMySQL(db).query_db(query, email_dict) # the data needs to in a dict 
        print("@@@ printing find_user results", results)
        if len(results) < 1:
            return False
        return cls(results[0])