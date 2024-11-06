from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class UserModel(BaseModel):
    email: str
    password: str
    balance: float | None = None


class UserSigninResponse(BaseModel):
    id: str
    email:str
    token: str


class UserSigninModel(BaseModel):
    email: str
    password: str

class UserResponseModel(BaseModel):
    id: str
    username: str
    email: str
    balance: float

class ProductModel(BaseModel):
    name: str
    price: float
    quantity: int
    description: Optional[str] = None

class ProductResponseModel(BaseModel):
    id: str
    name: str
    price: float
    quantity: int
    description: Optional[str] = None


class ResponseModel(BaseModel):
    status: int
    message: str


class FastAPIResponseWrapper(BaseModel):
    response: ResponseModel
    data: (
        UserResponseModel
        | List[UserResponseModel]
        | UserSigninResponse
        | None
    )