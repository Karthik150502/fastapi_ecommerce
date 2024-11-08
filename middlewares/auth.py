# import jwt
# from fastapi import FastAPI, Request
# from lib.config import JWT_SECRET
# from models.types import ResponseModel, UnAuthorizedResponse
# from models.response import Http
# from starlette.middleware.base import BaseHTTPMiddleware
# app = FastAPI()




# class AuthenticationError(Exception):
#     """Exception raised for authentication failures."""

#     def __init__(self, message="Authentication failed",reason=None):
#         """
#         Initializes the AuthenticationError.

#         Args:
#             message (str): A description of the error.
#             user_id (str, optional): The ID of the user who attempted to authenticate.
#             reason (str, optional): Specific reason for the failure, e.g., "Invalid token", "Expired session".
#         """

#         self.reason = reason
#         full_message = f"{message}"
#         if reason:
#             full_message += f" - Reason: {reason}"
#         super().__init__(full_message)


# def check_token(token: str):
#     try:
#         jwtPayload = jwt.decode(jwt=token,key=JWT_SECRET, algorithms=["HS256"])
#         return jwtPayload
#     except:    
#         raise AuthenticationError(reason="User token invalid")



# @app.middleware("http") 
# async def authenticate_user(request: Request, call_next):
#     print("The request route = ", request.url.path)
#     print("The request method = ", request.method)
#     print("The request headers = " , request.headers)
#     resuestBody = await request.body()
#     token = request.headers["authorization"].split(" ")[1]


#     match request.method:
#         case "POST":    
#             match request.url.path:
#                 case "/product":
#                     print("The request body for products = ")
#                 case "/user/onramp":
#                     try:
#                         jwtPayload = check_token(token)
#                     except AuthenticationError as error: 
#                         print("The user has requested to OnRamp some money....")
#                         return UnAuthorizedResponse(response=ResponseModel(status=Http.StatusForbidden, message="User Unauthorized."))
    


#     response = await call_next(request)
#     print(type(response))
#     return response
