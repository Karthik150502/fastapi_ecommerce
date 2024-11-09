import bcrypt 
import jwt 



from db.models import User, Product
from models.types import ProductModel, ResponseModel, ProductResponse
from models.response import Http
from sqlalchemy.orm import Session


from typing import List, Tuple
from lib.config import JWT_SECRET


def create_product(product: ProductModel, db: Session, user_id: str)-> Tuple[ResponseModel, ProductModel | None]:

    user = db.query(User).filter(User.id == user_id).first()
    data = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        image=product.image,
        added_by=user.id,
        sku=product.quantity
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return ResponseModel(status=200, message="Product created successfully"), product


