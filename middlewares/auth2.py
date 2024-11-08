import jwt
from fastapi import FastAPI, Request, HTTPException, Response
from lib.config import JWT_SECRET
from models.types import ResponseModel, UnAuthorizedResponse
from models.response import Http
from starlette.middleware.base import BaseHTTPMiddleware
app = FastAPI()



class AuthenticationError(Exception):



    """Exception raised for authentication failures."""

    def __init__(self, message="Authentication failed",reason=None):
        """
        Initializes the AuthenticationError.

        Args:
            message (str): A description of the error.
            user_id (str, optional): The ID of the user who attempted to authenticate.
            reason (str, optional): Specific reason for the failure, e.g., "Invalid token", "Expired session".
        """

        self.reason = reason
        full_message = f"{message}"
        if reason:
            full_message += f" - Reason: {reason}"
        super().__init__(full_message)


def check_token(token: str):
    try:
        jwtPayload = jwt.decode(jwt=token,key=JWT_SECRET, algorithms=["HS256"])
        return jwtPayload
    except:    
        raise AuthenticationError(reason="User token invalid")

class AuthenticationMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        print("The request route = ", request.url.path)
        print("The request method = ", request.method)
        print("The request headers = " , request.headers)
        resuestBody = await request.body()
        tokenString = request.headers.get("authorization", None)
        token = ""
        if tokenString:
            token = tokenString.split(" ")[1]

        match request.method:
            case "POST":
                match request.url.path:
                    case "/product":   
                        print("The request body for products = ")
                    case "/user/onramp":
                        try:
                            jwtPayload = check_token(token)
                        except:
                            return Response(
                                status_code=403,
                                content=str({
                                    "status":403,
                                    "message":"Not Authorized",
                                    "error": "Authentication failed",
                                })
                            )
                       

        response = await call_next(request)
        print(type(response))
        return response





app.add_middleware(AuthenticationMiddleware)
