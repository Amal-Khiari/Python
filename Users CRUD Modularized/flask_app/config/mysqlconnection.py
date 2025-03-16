# mysqlconnection.py
from flask import Flask
import pymysql.cursors

class MySQLConnection:
    def __init__(self, app):
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='your_password',
            db='your_database',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.connection = self.db

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                if query.lower().startswith("insert"):
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().startswith("select"):
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False