from Models.Database import dbController

connection = dbController.get_connection()
TBL_NAME = "users"

def get_users():
    try:
        with connection.cursor() as cursor:
            get_table = f"SELECT * FROM {TBL_NAME}"
            cursor.execute(get_table)
            result = cursor.fetchall()
            return result
    except TypeError as e:
        print(e)

def get_user(name):
    try:
        print("in users q")
        with connection.cursor() as cursor:
            print(name)
            query = f"SELECT * FROM {TBL_NAME} WHERE UserName = '{name}' LIMIT 1"
            cursor.execute(query)
            connection.commit()
            return cursor.fetchone()
    except TypeError as e:
        print(e)

 

#  

def get_breakdown():
    try:
        with connection.cursor() as cursor:
            get_categories_sum = f"SELECT TransactionCategory,SUM(TransactionAmount) AS categorySum FROM {TBL_NAME} GROUP BY TransactionCategory;"
            cursor.execute(get_categories_sum)
            result = cursor.fetchall()
            print(result)
            return result
    except TypeError as e:
        print(e)

def get_balance():
    try:
        with connection.cursor() as cursor:
            get_categories_sum = f"SELECT UserId ,SUM(TransactionAmount)  AS balance FROM {TBL_NAME} GROUP BY UserId;"
            cursor.execute(get_categories_sum)
            result = cursor.fetchall()
            print(result)
            return result
    except TypeError as e:
        print(e)

def add_transaction(transaction_details):
    try:
        with connection.cursor() as cursor:
            amount, vendor, category, userID = transaction_details
            query = f"INSERT INTO {TBL_NAME}(TransactionAmount,TransactionVendor,TransactionCategory,TransactionUserID) values (%s,%s,%s,%s)"
            params = (amount, vendor, category, userID)
            cursor.execute(query,params)
            connection.commit()
    except TypeError as e:
        print(e)

def delete_transaction(id):
    try:
        with connection.cursor() as cursor:
            query = f"DELETE FROM {TBL_NAME} WHERE TransactionID = '{id}' LIMIT 1"
            cursor.execute(query)
            connection.commit()
            return cursor.fetchall()
    except TypeError as e:
        print(e)

 
