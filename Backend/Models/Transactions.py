from Models.Database import transactions_queries as db


class Transactions:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

    def get_all(self):
        result = db.get_transactions()
        return result
    
    def add(self, tr_details):
        result = db.add_transaction(tr_details)
        return result

    def delete(self, tr_id):
        result = db.delete_transaction(tr_id)
        return result

    def get_balance(self):
        result = db.get_balance()
        return result

    
    def get_breakdown(self):
        result = db.get_breakdown()
        return result

    
    
