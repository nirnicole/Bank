from fastapi import APIRouter, HTTPException,Depends
from pydantic import BaseModel
from Routes import errorHandling
from Routes import input_validation
from Database import dbQueries
from auth.JWT_bearer import jwtBearer


router = APIRouter()
validator = input_validation.Validator()


class Transaction(BaseModel):
    amount: int
    vendor: str
    category: str

@router.get('/breakdown', status_code=200)
async def get_breakdown(user_id="0"):
    if validator.no_input(user_id) or not validator.is_numeric(user_id):
        raise HTTPException(status_code = 400, detail="Bad Request: invalid user id")
    else:
        try:
            res = dbQueries.get_breakdown()
            return {"breakdown":res}
        except:
            raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")


@router.get('/transactions', dependencies=[Depends(jwtBearer())], status_code=200)
async def get_transactions():
    try:
        res = dbQueries.get_transactions()
        return {"transactions":res}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")



@router.post('/transactions', status_code=201)
async def post_transaction(transaction: Transaction):
    try:
        transaction_details = [transaction.amount, transaction.vendor, transaction.category]
        dbQueries.add_transaction(transaction_details)
        return {"result": list(transaction_details)}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")



@router.delete('/transactions/{id}', status_code=202)
def delete_transaction(id):
    try:
        id=int(id)
        res = dbQueries.delete_transaction(id)
        print(res)
        return {"result": "deleted"}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")
