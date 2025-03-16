from flask import Flask
from flask_app.config.mysqlconnection import MySQLConnection

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    # Initialize the database connection
    MySQLConnection(app)

    # Register blueprints or routes here if needed

    return app