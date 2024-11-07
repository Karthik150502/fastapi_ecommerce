
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from db.database import getDb
from controllers.user import create_user_response, get_all_users_response, get_single_user_response, signin
from models.response import Http
from models.schema import UserModel, UserSigninModel, FastAPIResponseWrapper, ResponseModel
from middlewares.auth import authenticate_user



Router = APIRouter(
    prefix="/users",
)



@Router.post("/signup", response_model=FastAPIResponseWrapper)
async def create_user(user: UserModel, db: Session = Depends(getDb)):
    response, data = create_user_response(user, db)
    return FastAPIResponseWrapper(response=response, data=data)


@Router.get("/{userid}", response_model=FastAPIResponseWrapper)
def get_users(userid: str, db: Session = Depends(getDb)):
    response = ResponseModel(status=Http.StatusOk, message="User Fetched successfully.")
    data = {
            "id": userid,
            "username": userid,
            "email": userid,
            "balance": 0.00 
    }
    return FastAPIResponseWrapper(response=response, data=data)




@Router.get("/", response_model=FastAPIResponseWrapper)
def get_all_users(db: Session = Depends(getDb)):
    response, data = get_all_users_response(db)
    return FastAPIResponseWrapper(response=response, data=data)


@Router.post("/signin", response_model=FastAPIResponseWrapper)
def get_all_users(user: UserSigninModel, db: Session = Depends(getDb)):
    return signin(db, user)


@Router.get("/{userid}", response_model=FastAPIResponseWrapper)
def get_all_users(userid: str, db: Session = Depends(getDb)):
    response, data = get_single_user_response(db, userid)
    return FastAPIResponseWrapper(response=response, data=data)


