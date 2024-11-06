from dotenv import load_dotenv
import os
load_dotenv()







JWT_SECRET = os.getenv("JWT_SECRET")
DATABASE_URL = os.getenv("DATABASE_URL")







