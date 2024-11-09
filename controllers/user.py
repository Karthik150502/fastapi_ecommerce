import bcrypt
import jwt
from db.models import User
from models.types import UserModel, UserResponseModel, ResponseModel, UserSigninModel, UserSigninResponse, FastAPIResponseWrapper, UserOnRamp, UserOnRampResponse
from models.response import Http
from sqlalchemy.orm import Session

from typing import List
from lib.config import JWT_SECRET



def create_user_response(user: UserModel, db: Session) -> tuple[ResponseModel, UserResponseModel | None]:
    db_user = db.query(User).filter(User.email == user.email).first()
    if(db_user):
        return ResponseModel(status=Http.StatusBadRequest, message="User already exists"), None
    
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    

    user = User(
        email=user.email, 
        password_hash=hashed_password, 
    )
    db.add(user)
    db.commit()

    user_response = UserResponseModel(
        id=str(user.id),
        username=user.email,
        email=user.email,
        balance=user.balance
    )

    return ResponseModel(status=Http.StatusOk, message="User created successfully."), user_response


def get_all_users_response(db:Session) -> tuple[ResponseModel, List[UserResponseModel]]:
    users = db.query(User).all()    
    response = ResponseModel(status=Http.StatusOk, message="User singed up successfully.")
    result = [
        UserResponseModel(
            id=str(user.id),
            username=user.email,
            email=user.email,
            balance=user.balance
        )
        for user in users
    ]
    return response, result
        
def get_single_user_response(db:Session, userid:str) -> tuple[ResponseModel, UserResponseModel]:
    user = db.query(User).filter(User.id == userid).first()
    response = ResponseModel(status=Http.StatusOk, message="User signed in successfully.")
    result = UserResponseModel(
        id=str(user.id),
        username=user.email,
        email=user.email,
        balance=user.balance
    )
    return response, result

def signin(db: Session, user: UserSigninModel):
    userExists = db.query(User).filter(User.email == user.email).first()
    if not userExists:
        return FastAPIResponseWrapper(response=ResponseModel(status=Http.StatusNotFound, message="User does not exist."))
    
    passwordCorrect = bcrypt.checkpw(user.password.encode("utf-8"), userExists.password_hash.encode("utf-8"))

    if not passwordCorrect:
        return FastAPIResponseWrapper(response=ResponseModel(status=Http.StatusUnauthorized, message="Incorrect password."))

    jwtPayload = {
        "id": str(userExists.id),
        "email": userExists.email
    }   

    token = jwt.encode(payload=jwtPayload,key=JWT_SECRET)

    userSigninResponse = UserSigninResponse(id=str(userExists.id), email=userExists.email, token="Bearer " + token)
    response = ResponseModel(status=Http.StatusOk, message="User logged in successfully.")  
    return FastAPIResponseWrapper(response=response, data=userSigninResponse)
    

def onramp_user(db: Session, data: UserOnRamp, userid: str)-> tuple[ResponseModel, UserOnRampResponse]:

    user = db.query(User).filter(User.id == userid).first()
    if(not user):
        response = ResponseModel(status=Http.StatusBadRequest, message="User not found.")
        return response, None


    user.balance = float(user.balance) + data.amount
    db.commit()
    db.refresh(user)   
    response = ResponseModel(status=Http.StatusOk, message="User onramped successfully.")
    res = UserOnRampResponse(amount=data.amount, userid=str(user.id), current_balance=user.balance)
    return response, res









