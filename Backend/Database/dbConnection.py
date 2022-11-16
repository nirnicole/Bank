import pymysql
DB_NAME = "bank_app"

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db=DB_NAME,
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

