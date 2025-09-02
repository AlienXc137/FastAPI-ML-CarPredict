from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import create_token

router = APIRouter() # Define the router for authentication-related routes
#router is a modular grouping of routes that you attach to app.

class AuthInput(BaseModel):
    username: str
    password: str

@router.post('/login') # Define a POST endpoint for user login
def login(auth: AuthInput): # Accepts an AuthInput model containing username and password
    if (auth.username == 'admin') and (auth.password == 'admin'):
        token = create_token({'sub': auth.username}) # Create a token if credentials are valid
        return {'access_token': token}
    return {'error': 'Invalid Credentials'}