import bcrypt
import jwt
from db.models import User
from models.schema import ProductModel, ResponseModel, ProductResponse
from models.response import Http
from sqlalchemy.orm import Session

from typing import List
from lib.config import JWT_SECRET





def create_product(product: ProductModel, db: Session)-> ResponseModel:
    return ResponseModel(status=200, message="Product created successfully")


