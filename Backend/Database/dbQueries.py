from Database.dbConnection import connection

TBL_NAME = "transactions"

def get_transactions():
    try:
        with connection.cursor() as cursor:
            get_table = f"SELECT * FROM {TBL_NAME}"
            cursor.execute(get_table)
            result = cursor.fetchall()
            return result
    except TypeError as e:
        print(e)

def get_breakdown():
    try:
        with connection.cursor() as cursor:
            get_categories_sum = f"SELECT TransactionCategory,SUM(TransactionAmount)  AS categorySum FROM {TBL_NAME} GROUP BY TransactionCategory;"
            cursor.execute(get_categories_sum)
            result = cursor.fetchall()
            print(result)
            return result
    except TypeError as e:
        print(e)

def add_transaction(transaction_details):
    try:
        with connection.cursor() as cursor:
            amount, vendor, category = transaction_details
            query = f"INSERT INTO {TBL_NAME}(TransactionAmount,TransactionVendor,TransactionCategory) values (%s,%s,%s)"
            params = (amount, vendor, category)
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

