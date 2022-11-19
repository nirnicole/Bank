import pymysql
from Models.Database import dbInitializer
DB_NAME = "bank_app"


class DBController:
    def __init__(self):
        self.connection = None

    def run_init_script(self):
        dbInitializer.init_script()

    def get_connection(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db=DB_NAME,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.connection = connection
        return connection
    
    def close_connection(self):
        self.connection.close()

