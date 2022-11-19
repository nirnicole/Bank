from Models.Database import transactions_queries as tdb
from Models.Database import users_queries as udb


class Transactions:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

    def get_all(self):
        result = tdb.get_transactions()
        return result
    
    def add(self, transaction):
        user_name = transaction.user
        print(user_name)
        user_ID = udb.get_user(user_name)
        print(user_ID)
        transaction_details = [transaction.amount, transaction.vendor, transaction.category, user_ID]
        result = tdb.add_transaction(transaction_details)
        return result

    def delete(self, tr_id):
        result = tdb.delete_transaction(tr_id)
        return result

    def get_balance(self):
        result = tdb.get_balance()
        return result

    
    def get_breakdown(self):
        result = tdb.get_breakdown()
        return result

    
    
