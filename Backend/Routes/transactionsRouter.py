from fastapi import APIRouter, HTTPException,Depends
from Models.Transactions import Transactions
from auth.JWT_bearer import jwtBearer
from Schemas.Transaction import Transaction

router = APIRouter(dependencies=[Depends(jwtBearer())])
model_transactions = Transactions()

@router.get('/breakdown', status_code=200)
async def get_breakdown(user_id="0"):
    try:
        res = model_transactions.get_breakdown()
        return {"breakdown":res}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")


@router.get('/transactions', status_code=200)
async def get_transactions():
    try:
        res = model_transactions.get_all()
        return {"transactions":res}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")



@router.post('/transactions', status_code=201)
async def post_transaction(transaction: Transaction):
    try:
        print(transaction)
        model_transactions.add(transaction)
        return {"result": list(transaction)}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")



@router.delete('/transactions/{id}', status_code=202)
def delete_transaction(id):
    try:
        id=int(id)
        res = model_transactions.delete(id)
        print(res)
        return {"result": "deleted"}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")
