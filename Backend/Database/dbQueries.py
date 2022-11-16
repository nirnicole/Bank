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

# def insert_record(record):
#     try:
#         with connection.cursor() as cursor:
#             query = f"INSERT IGNORE INTO recipes values({record})"
#             cursor.execute(query)
#             connection.commit()
#     except TypeError as e:
#         print(e)

# def ing_exist(table, column, val):
#     cur = connection.cursor()
#     cur.execute(f"SELECT {column} FROM {table} WHERE {column} = '{val}' LIMIT 1")
#     if cur.fetchone():
#         return True
#     else:
#         return False

