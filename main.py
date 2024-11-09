from typing import Union, Coroutine, Any
from uuid import uuid4
from fastapi import FastAPI
from jinja2 import Template

import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from api.users import Router as users_router
from api.products import ProductRouter
from api.purchases import PurchasesRouter
# from middlewares.auth import authenticate_user
from functools import partial
from middlewares.auth import AuthenticationMiddleware
app = FastAPI()



# auth: partial[Coroutine[Any, Any, Any]] = partial(authenticate_user)
# app.middleware("http")(auth)




app.add_middleware(AuthenticationMiddleware)

@app.get("/")
def respond():
    return {"status": 200}


app.include_router(users_router, tags=["users"])
app.include_router(ProductRouter, tags=["products"])
app.include_router(PurchasesRouter, tags=["purchases"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)