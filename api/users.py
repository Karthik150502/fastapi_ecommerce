
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import getDb
from controllers.user import create_user_response, get_all_users_response, get_single_user_response, signin
from models.response import Http

from models.schema import UserModel, UserSigninModel, FastAPIResponseWrapper, ResponseModel

Router = APIRouter()




@Router.post("/user", response_model=FastAPIResponseWrapper)
def create_user(user: UserModel, db: Session = Depends(getDb)):
    response, data = create_user_response(user, db)
    return FastAPIResponseWrapper(response=response, data=data)




@Router.get("/user/{userid}", response_model=FastAPIResponseWrapper)
def get_users(userid: str, db: Session = Depends(getDb)):
    response = ResponseModel(status=Http.StatusOk, message="User Fetched successfully.")
    data = {
            "id": userid,
            "username": userid,
            "email": userid,
            "balance": 0.00 
    }
    return FastAPIResponseWrapper(response=response, data=data)




@Router.get("/users", response_model=FastAPIResponseWrapper)
def get_all_users(db: Session = Depends(getDb)):
    response, data = get_all_users_response(db)
    return FastAPIResponseWrapper(response=response, data=data)


@Router.post("/users/signin", response_model=FastAPIResponseWrapper)
def get_all_users(user: UserSigninModel, db: Session = Depends(getDb)):
    return signin(db, user)


@Router.get("/users/{userid}", response_model=FastAPIResponseWrapper)
def get_all_users(userid: str, db: Session = Depends(getDb)):
    response, data = get_single_user_response(db, userid)
    return FastAPIResponseWrapper(response=response, data=data)


