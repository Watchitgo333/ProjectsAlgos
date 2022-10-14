from FlaskApp import app
from FlaskApp.Configuration.mysqlconnection import connectToMySQL
from flask import flash
#from flask.ext.bcrypt import Bcrypt
import bcrypt
#from FlaskA.Model.Sighting import Sighting
import re

#bcrypt = Bcrypt (app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
DB = "pokemon_schema"
pokemon_1 = ["Zacian", "Lunala", "Calyrex - Shadow Rider", "Calyrex - Ice Rider"]
pokemon_2 = ["Groudon", "Kyogre", "Dialga", "Palkia", "Yveltal"]
pokemon_3 = ["Incineroar", "Landorus"]
pokemon_4 = ["Rillaboom", "Amoonguss", "Whimsicott", "Shedinja", "Celesteela"]
pokemon_5 = ["Grimmsnarl", "Gastrodon", "Porygon2", "Indeedee"]
pokemon_6 = ["Charizard", "Regieleki", "Thundurus", "Tornadus", "Galarian Moltres"]

class User:
    def __init__ (self, user):
        self.id = user ["id"]
        # self.first_name = user ["first_name"]
        # self.last_name = user ["last_name"]
        self.username = user ["username"]
        self.email = user ["email"]
        self.password = user ["password"]
        self.placement = user ["placement"]
        self.pokemon_1 = user ["pokemon_1"]
        self.pokemon_2 = user ["pokemon_2"]
        self.pokemon_3 = user ["pokemon_3"]
        self.pokemon_4 = user ["pokemon_4"]
        self.pokemon_5 = user ["pokemon_5"]
        self.pokemon_6 = user ["pokemon_6"]

    @classmethod
    def get_by_email (cls, email):

        data = {
            "email": email
        }
        query = "SELECT * FROM users_db WHERE email = %(email)s;"
        result = connectToMySQL (DB).query_db (query, data)
        if len (result) < 1:
            return False
        return cls (result [0])
    
    @classmethod
    def get_by_ID (cls, userID):

        data = {"id": userID}
        query = "SELECT * FROM users_db WHERE id = %(id)s;"
        result = connectToMySQL (DB).query_db (query, data)

        if len (result) < 1:
            return False
        return cls (result [0])

    @classmethod
    def get_all (cls):
        query = "SELECT * from users_db;"
        user_data = connectToMySQL (DB).query_db (query)

        users = []
        for user in user_data:
            users.append (cls (user))
        return users
        
    @classmethod
    def create_valid_user (cls, user):
        # Validate user
        print(user)
        if not cls.is_valid (user):
            print(cls.is_valid)
            return False
        # Hash password
        #pw_hash = bcrypt.generate_password_hash (user ['password'])
        pw_hash = bcrypt.hashpw (user['password'].encode ('UTF-8'), bcrypt.gensalt())
        user = user.copy ()
        user ["password"] = pw_hash
        print ("User after adding pw: ", user)
        # Insert user into DB
        query = """
        INSERT into users_db (username, email, password) VALUES (%(username)s, %(email)s, %(password)s);
        """
        # query = """
        #         INSERT into users (first_name, last_name, username, email, password) VALUES (%(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password)s);
        #         """

        new_user_id = connectToMySQL (DB).query_db (query, user)
        new_user = cls.get_by_ID (new_user_id)

        return new_user
    
    @classmethod 
    def authenticated_user_by_input (cls, user_input):
        valid = True
        existing_user = cls.get_by_email (user_input ["email"])
        password_valid = True

        if not existing_user:
            valid = False
        else:
            #password_valid = bcrypt.check_password_hash(existing_user.password, user_input ['password']) 
            print (user_input ['password'].encode ('UTF-8'))
            print (existing_user.password)
            encoded_user_password = user_input ['password'].encode ('UTF-8')
            password_valid = bcrypt.checkpw (encoded_user_password, existing_user.password.encode ('UTF-8'))
            if not password_valid:
                valid = False
        if not valid:
            flash ("That email & password combination does not match our records", "login")
            return False
        return existing_user

    @classmethod
    def is_valid (cls, user):
        valid = True

        # if len (user ["first_name"]) < 2:
        #     valid = False
        #     flash ("First name must be at least 2 characters")
        # if len (user ["last_name"]) < 2:
        #     valid = False
        #     flash ("Last name must be at least 2 characters") 
        if len (user ["username"]) <= 0:
            valid = False
            flash ("Invalid username!", "register")
        if not EMAIL_REGEX.match (user ['email']): 
            flash ("Invalid email address!", "register")
            valid = False
        if len (user ["password"]) < 8:
            valid = False
            flash ("Password must be at least 8 characters long", "register")
        if not user ["password"] == user ["confirm"]:
            flash ("Did you have a typo? Passwords must match", "register")
            valid = False

        email_already_has_account = User.get_by_email (user ["email"])
        if email_already_has_account:
            flash ("An account with that email already exists, please log in.","register")
            valid = False

        return valid

    @classmethod
    def createTeam (cls, pokeDet, user):
        if not cls.is_team_valid (pokeDet):
            return False, 0
        print (pokeDet)
        username = pokeDet ["username"]
        pokemon_1 = pokeDet ["pokemon_1"]
        pokemon_2 = pokeDet ["pokemon_2"]
        pokemon_3 = pokeDet ["pokemon_3"]
        pokemon_4 = pokeDet ["pokemon_4"]
        pokemon_5 = pokeDet ["pokemon_5"]
        pokemon_6 = pokeDet ["pokemon_6"]
        query = """INSERT INTO users_db (username, pokemon_1, pokemon_2, pokemon_3, pokemon_4, pokemon_5, pokemon_6) VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}");""".format (username, pokemon_1, pokemon_2, pokemon_3, pokemon_4, pokemon_5, pokemon_6)

        # query = """INSERT INTO user_db (username, pokemon_1, pokemon_2, pokemon_3, pokemon_4, pokemon_5, pokemon_6) VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}");""".format (username, pokemon_1, pokemon_2, pokemon_3, pokemon_4, pokemon_5, pokemon_6)
        print (query)
        pokeID = connectToMySQL (DB).query_db (query, pokeDet)
        return True, pokeID

    @classmethod
    def editTeam (cls, pokeDet, session_id):
        print (pokeDet)
        if not cls.is_team_valid (pokeDet):
            return False
        userID = pokeDet ["id"]
        pokemon_1 = pokeDet ["pokemon_1"]
        pokemon_2 = pokeDet ["pokemon_2"]
        pokemon_3 = pokeDet ["pokemon_3"]
        pokemon_4 = pokeDet ["pokemon_4"]
        pokemon_5 = pokeDet ["pokemon_5"]
        pokemon_6 = pokeDet ["pokemon_6"]
        query = """UPDATE users_db
                    SET pokemon_1 = "{0}", pokemon_2 = "{1}", pokemon_3 = "{2}", pokemon_4 = "{3}", pokemon_5 = "{4}", pokemon_6 = "{5}" WHERE id = {6};""".format (pokemon_1, pokemon_2, pokemon_3, pokemon_4, pokemon_5, pokemon_6, userID)
        print (query)
        
        result = connectToMySQL (DB).query_db (query)
        poke = cls.get_by_ID (pokeDet ["id"])
        return poke

    @classmethod
    def delete_user_by_id (cls, userID):

        data = {"id": userID}
        query = "DELETE from users_db WHERE id = %(id)s;"
        connectToMySQL (DB).query_db (query, data)

        return userID

    @staticmethod
    def is_team_valid (pokeDet):
        valid = True
        flash_string = "All fields are required"
        error_message = ""

        if len (pokeDet ["username"]) <= 0:
            valid = False
            error_message = "This field must be filled out"
            flash ("This field must be filled out")
        if (pokeDet ["pokemon_1"]) not in pokemon_1:
            valid = False
            error_message = "Please choose a pokemon from the list provided"
            # flash ("Please choose a pokemon from the list provided", "pokemon")
        if (pokeDet ["pokemon_2"]) not in pokemon_2:
            valid = False
            error_message = "Please choose a pokemon from the list provided"
            # flash ("Please choose a pokemon from the list provided", "pokemon")
        if (pokeDet ["pokemon_3"]) not in pokemon_3:
            valid = False
            error_message = "Please choose a pokemon from the list provided"
            # flash ("Please choose a pokemon from the list provided", "pokemon")
        if (pokeDet ["pokemon_4"]) not in pokemon_4:
            valid = False
            error_message = "Please choose a pokemon from the list provided"
            # flash ("Please choose a pokemon from the list provided", "pokemon")
        if (pokeDet ["pokemon_5"]) not in pokemon_5:
            valid = False
            error_message = "Please choose a pokemon from the list provided"
            # flash ("Please choose a pokemon from the list provided", "pokemon")
        if (pokeDet ["pokemon_6"]) not in pokemon_6:
            valid = False
            error_message = "Please choose a pokemon from the list provided"
            # flash ("Please choose a pokemon from the list provided", "pokemon")
        print (error_message)
        return valid

    # @staticmethod
    # def is_team_valid (pokeDet):
    #     valid = True
    #     flash_string = "All fields are required"

    #     if len (pokeDet ["username"]) <= 0:
    #         valid = False
    #         error_message = "This field must be filled out"
    #         flash ("This field must be filled out")
    #     if (pokeDet ["pokemon_1"]) not in pokemon_1:
    #         valid = False
    #         error_message = "Please choose a pokemon from the list provided"
    #         flash ("Please choose a pokemon from the list provided")
    #     if (pokeDet ["pokemon_2"]) not in pokemon_2:
    #         valid = False
    #         error_message = "Please choose a pokemon from the list provided"
    #         flash ("Please choose a pokemon from the list provided")
    #     if (pokeDet ["pokemon_3"]) not in pokemon_3:
    #         valid = False
    #         error_message = "Please choose a pokemon from the list provided"
    #         flash ("Please choose a pokemon from the list provided")
    #     if (pokeDet ["pokemon_4"]) not in pokemon_4:
    #         valid = False
    #         error_message = "Please choose a pokemon from the list provided"
    #         flash ("Please choose a pokemon from the list provided")
    #     if (pokeDet ["pokemon_5"]) not in pokemon_5:
    #         valid = False
    #         error_message = "Please choose a pokemon from the list provided"
    #         flash ("Please choose a pokemon from the list provided")
    #     if (pokeDet ["pokemon_6"]) not in pokemon_6:
    #         valid = False
    #         error_message = "Please choose a pokemon from the list provided"
    #         flash ("Please choose a pokemon from the list provided")

    #     return valid