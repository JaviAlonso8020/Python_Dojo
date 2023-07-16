# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
#might need other imports like flash other classes and regex
from flask_app.models import ninja_model  #we do not import the class


db = 'dojos_and_ninjas_schema'

# model the class after the friend table from our database
class Dojo:
    def __init__(self, data):
        #follow database table fields plus any other attribute you want to create
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    def __repr__(self) -> str:  #this is optional to help debug
        return f" Dojo Repr --> {self.id} {self.name};Ninjas {self.ninjas}"
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos (name)
                VALUES ( %(name)s)
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one(cls, dojo_id):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {'id': dojo_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        print('dojo_results****jar',results) 
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_dojo_with_ninjas(cls,dojo_id):
        data = {
            "id" : dojo_id
        }
        query = """SELECT * FROM dojos 
                LEFT JOIN ninjas on ninjas.dojo_id = dojos.id 
                WHERE dojos.id = %(id)s;
                """  
        results = connectToMySQL(db).query_db(query,data) #results is dictionary 
        dojo_result = cls(results[0]) #this is becuase Dojo comes up on every row
                                #as an object
        for ninja_in_dojo in results:
            ninja_one_dojo = {
                "id": ninja_in_dojo["ninjas.id"],
                "dojo_id": ninja_in_dojo["dojo_id"],
                "first_name": ninja_in_dojo["first_name"],
                "last_name": ninja_in_dojo["last_name"],
                "age": ninja_in_dojo["age"],
                "created_at": ninja_in_dojo["ninjas.created_at"],
                "updated_at": ninja_in_dojo["ninjas.updated_at"],
            }
            dojo_result.ninjas.append(ninja_model.Ninja(ninja_one_dojo))
            # this adds a list of ninja objects into the object of the dojo
        return dojo_result
    
