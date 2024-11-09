
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from db.database import getDb
from controllers.user import create_user_response, get_all_users_response, get_single_user_response, signin, onramp_user
from models.response import Http
from models.types import UserModel, UserSigninModel, FastAPIResponseWrapper, ResponseModel, UserOnRamp, AuthToken
from middlewares.auth import get_user


Router = APIRouter(
    prefix="/user",
)



@Router.post("/signup", response_model=FastAPIResponseWrapper)
async def create_user(user: UserModel, db: Session = Depends(getDb)):
    response, data = create_user_response(user, db)
    return FastAPIResponseWrapper(response=response, data=data)


@Router.post("/onramp", response_model=FastAPIResponseWrapper)
def user_onramp(body: UserOnRamp,  request: Request, db: Session = Depends(getDb)):
    token = request.headers["authorization"].split(" ")[1]
    jwtpayload = get_user(token)
    response, data = onramp_user(db, body, jwtpayload["id"])
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


