from flask_app.config.mysqlconnection import connectToMySQL
import re # the regex module

# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import Flask
class user:
    db = "login_reg"
    def __init__(self,data):
        self.id =data['id']
        self.first_name =data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

@classmethod
def save(cls,data):
    query = " INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
    return connectToMySQL(cls.db).query_db(query,data)
@classmethod
def get_all(cls):
    query = "SELECT * FROM users;"
    results = connectToMySQL(cls.db).query_db(query)
    users = []
    for row in results:
        users.append(cls[row])
    return users 
    
@classmethod
def get_by_email(cls,data):
    query=" SELECT * FROM users WHERE email =%(email)s;"
    results = connectToMySQL(cls.db).query_db(query,data)
    return cls(results[0])

staticmethod
def valdation_register(user):
    is_valid= True
    query = "SELECT * FROM users WHERE email=%(email)s;"
    results = connectToMySQL(user.db).query_db(query,user)
    if len(results) >= 1 : 
        flash("Email is already taken. ")
        is_valid = False
    if not EMAIL_REGEX.match(user['email']):
        falsh("Invalid Email !!! ","register")
        is_valid=False
    if len(user['first_name']) < 3:
        falsh("first name must be at least 3 caracters","register")
        is_valid= False   
    if len(user['last_name']) < 3:
        falsh(" last name must be at least 3 caracters", "register")
        is_valid= False 
    if len(user['password']) < 8:
        falsh("password must be at least 8 caracters","register")
        is_valid= False
    if user['password'] != user['confirm']:
        flash ("passwords don't match","register")
                        
    return is_valid        

