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


class UserOnRamp(BaseModel):
    amount:int


class UserOnRampResponse(BaseModel):
    amount: int
    userid: int
    current_balance:int


class ProductModel(BaseModel):
    name: str
    price: float
    quantity: int
    image: Optional[str] = None
    description: Optional[str] = None
    added_by: str


class ProductResponse(BaseModel):
    id: str
    name: str
    price: float
    quantity: int
    image: Optional[str] = None
    description: Optional[str] = None
    added_by: str
    created_at: datetime
    updated_at: datetime


class UserSigninModel(BaseModel):
    email: str
    password: str

class UserResponseModel(BaseModel):
    id: str
    username: str
    email: str
    balance: float



class ResponseModel(BaseModel):
    status: int
    message: str


class FastAPIResponseWrapper(BaseModel):
    response: ResponseModel
    data: (
        UserResponseModel
        | List[UserResponseModel]
        | UserSigninResponse 
        | List[ProductResponse] 
        | UserOnRampResponse
        | None
    )


class ProductResponse(BaseModel):
    response: ResponseModel
    data: ProductResponse | None


class UnAuthorizedResponse(BaseModel):
    response: ResponseModel