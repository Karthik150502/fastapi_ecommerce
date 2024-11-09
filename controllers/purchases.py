from db.models import User, Product, UserPurchases
from models.types import ResponseModel, PurchaseResponse, PurchaseModel
from models.response import Http
from sqlalchemy.orm import Session


from typing import Tuple


def purchase_product(purchase: PurchaseModel, db: Session, user_id: str)-> Tuple[ResponseModel, PurchaseResponse | None]:

    user = db.query(User).filter(User.id == user_id).first()

    product = db.query(Product).filter(Product.id == purchase.product_id).first()
    if(product.sku < purchase.quantity):
        return ResponseModel(status=Http.StatusServiceUnavailable, message="Out of stock"), None

    price_needed = product.price * purchase.quantity
    if(price_needed > user.balance):
        return ResponseModel(status=Http.StatusServiceUnavailable, message="Insufficient Balance"), None
        
    data = UserPurchases(
        product_id = product.id,
        user_id = user.id,
        quantity = purchase.quantity
    )

    product.sku = product.sku - purchase.quantity
    user.balance = user.balance - price_needed 
    db.add(data)
    db.commit()
    db.refresh(data)
    return ResponseModel( status=Http.StatusOk, message="Product purchased successfully"), PurchaseResponse(
        user_id = str(user.id),
        product_id = str(product.id),
        quantity = purchase.quantity,
        price = product.price
    )


