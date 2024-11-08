
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from db.database import getDb
from controllers.products import create_product 
from models.response import Http

from models.types import ProductModel, FastAPIResponseWrapper


ProductRouter = APIRouter(
    prefix="/product",
)


@ProductRouter.post("/", response_model=FastAPIResponseWrapper)
async def createProduct(product: ProductModel, db: Session = Depends(getDb)):
    response = create_product(product, db)
    return FastAPIResponseWrapper(response=response, data=None)

    
