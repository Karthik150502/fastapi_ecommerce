from typing import Union
from uuid import uuid4
from fastapi import FastAPI
from jinja2 import Template

import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from api.users import Router as users_router
app = FastAPI()



@app.get("/")
def respond():
    return {"status": 200}


app.include_router(users_router, tags=["users"])



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)