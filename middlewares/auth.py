import time

from fastapi import FastAPI, Request
from models.schema import UserModel
from typing import Union


app = FastAPI()


@app.middleware("http") 
async def authenticate_user(request: Request, call_next):
    print("The request route = ", request.url.path)
    print("The request method = ", request.method)

    match request.method:
        case "POST":
            match request.url.path:
                case "/product":
                    print("The request body for products = ", await request.body())

    


    response = await call_next(request)
    return response
