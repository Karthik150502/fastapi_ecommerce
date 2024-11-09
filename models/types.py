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
    amount:float


class UserOnRampResponse(BaseModel):
    amount: float
    userid: str
    current_balance: float


class ProductModel(BaseModel):
    name: str
    price: float
    quantity: int
    image: Optional[str] = None
    description: Optional[str] = None




class AuthToken(BaseModel):
    token: str


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


class PurchaseModel(BaseModel):
    product_id: str
    quantity: int

class PurchaseResponse(BaseModel):
    user_id: str
    product_id: str
    quantity: int
    price: float


class UserResponseModel(BaseModel):
    id: str
    username: str
    email: str
    balance: float



class ResponseModel(BaseModel):
    status: int
    message: str | dict


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


class ProductCreateResponse(BaseModel):
    response: ResponseModel
    data: ProductModel | None


class PurchaseResponseWrapper(BaseModel):
    response: ResponseModel
    data: (PurchaseResponse | None)



class UnAuthorizedResponse(BaseModel):
    response: ResponseModel