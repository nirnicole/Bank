import pymysql
from Models.Database import dbInitializer

DB_NAME = "bank_app"
running = False
connection = None

def run_init_script():
    global running
    if not running:
        dbInitializer.init_script()
        running = True

def get_connection():
    global connection
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db=DB_NAME,
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def close_connection():
    global connection
    global running
    connection.close()
    running = False

