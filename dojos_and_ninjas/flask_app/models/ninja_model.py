# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
#might need other imports like flash other classes and regex

db = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__(self, data):
        #follow database table fields plus any other attribute you want to create
        self.id = data['id']
        self.dojo_id = data['dojo_id']  #I was missing this when Ninja showed no attribute
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self) -> str:  #this is optional to help debug
        return f" Ninja Repr - -> {self.id} {self.dojo_id} {self.first_name}"

    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (dojo_id, first_name, last_name,
                age)
                VALUES ( %(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
                # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(db).query_db(query)
        print(results)       
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninja
    
    @classmethod
    def get_ninja_dojo(cls, data):
        query = """SELECT dojo_id FROM
                ninjas WHERE id = %(id)s;
                """
        query_data = {
            "id" : data
        }
        dojo_dict = connectToMySQL(db).query_db(query, query_data) #this requires to pass a dict
        return dojo_dict[0]['dojo_id']
