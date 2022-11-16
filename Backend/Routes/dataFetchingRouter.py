from fastapi import APIRouter, HTTPException,Request
from pydantic import BaseModel
from Routes import errorHandling
from Routes import input_validation
from Database import dbQueries

router = APIRouter()
validator = input_validation.Validator()

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


@router.get('/transactions', status_code=200)
async def get_transactions(user_id="0"):
    if validator.no_input(user_id) or not validator.is_numeric(user_id):
        raise HTTPException(status_code = 400, detail="Bad Request: invalid user id")
    else:
        try:
            res = dbQueries.get_transactions()
            return {"transactions":res}
        except:
            raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")



# @router.post('/insource/')
# async def post(request: Request):
#     global caching_metadata
#     response = await request.json()   
#     key = list(response.keys())[0]     
#     val = response[key]
#     dbQueries.create_number(key, val)

#     print(response)
#     return response

# @router.delete('/insource/{item_id}')
# def delete(item_id):
#     global caching_metadata
#     item_id=int(item_id)
#     item = caching_metadata[item_id]
#     del caching_metadata[item_id]
#     return item