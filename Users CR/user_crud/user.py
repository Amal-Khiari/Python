from mysqlconnection import connectToMySQL
class User:
    db = "name"
    def __init__(self, dict):
        self.id = dict['id']
        self.first_name = dict['first_name']
        self.last_name = dict['last_name']
        self.email = dict['email']
        self.created_at = dict['created_at']
        self.updated_at = dict['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(cls.db).query_db(query)
        users_list = []
        for row in result:
            users_list.append(cls(row))
        return users_list
    
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """
        connectToMySQL(cls.db).query_db(query, data)