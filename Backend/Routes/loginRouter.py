from fastapi import APIRouter, HTTPException, Body, Depends
from pydantic import BaseModel, Field
from Routes import errorHandling
from Routes import input_validation
from auth.jwt_handler import signJWT

router = APIRouter()
validator = input_validation.Validator()

users = []


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo":{
                "title":"some title about animals",
                "content":"some content about animals"
            }
        }

class UserSchema(BaseModel):
    user: str = Field(default=None)
    pwd: str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "user" : "nir",
                "pwd" : "ucode"
            }
        }

class UserLoginSchema(BaseModel):
    user: str = Field(default=None)
    pwd: str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "user" : "nir",
                "pwd" : "ucode"
            }
        }


# @router.post('/auth', status_code=200)
# async def get_breakdown():
#     try:
#         res = {}
#         return {"breakdown":res}
#     except:
#         raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")


@router.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.user)

def check_user(data:UserLoginSchema):
    for user in users:
        if user.user == data.user and user.pwd == data.pwd:
            return True
    return False

@router.post("/user/login", tags=["user"])
def user_login(user:UserLoginSchema = Body()):
    if check_user(user):
        return signJWT(user.user)
    else:
        return {
            "error": "invalid login details!"
        }