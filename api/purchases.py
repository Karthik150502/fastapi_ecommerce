
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from db.database import getDb
from controllers.purchases import purchase_product 

from models.types import PurchaseModel, PurchaseResponseWrapper
from middlewares.auth import get_user


PurchasesRouter = APIRouter(
    prefix="/purchase",
)




@PurchasesRouter.post("/", response_model=PurchaseResponseWrapper)
async def createProduct(purchase: PurchaseModel, request: Request,  db: Session = Depends(getDb)):
    token = request.headers["authorization"].split(" ")[1]
    jwtpayload = get_user(token)
    response, data = purchase_product(purchase, db, jwtpayload["id"])
    return PurchaseResponseWrapper(response=response, data=data)

