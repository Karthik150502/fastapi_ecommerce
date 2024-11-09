
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import List, Union
from db.database import getDb
from controllers.products import create_product 
from models.response import Http

from models.types import ProductModel, ProductCreateResponse
from middlewares.auth import get_user
from models.types import AuthToken


ProductRouter = APIRouter(
    prefix="/product",
)


@ProductRouter.post("/", response_model=ProductCreateResponse)
async def createProduct(product: ProductModel, request: Request,  db: Session = Depends(getDb)):
    token = request.headers["authorization"].split(" ")[1]
    jwtpayload = get_user(token)
    response, data = create_product(product, db, jwtpayload["id"])
    return ProductCreateResponse(response=response, data=data)

    
