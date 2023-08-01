from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    name:str
    email:str
    phone:str
    password:str
    shopname:str
    gst:int

class Login(BaseModel):
    email : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class Info(BaseModel):
    id:int

class Update(BaseModel):
    id:int
    name:str
    email:str
    phone:str
    shopname:str
    gst:int
    updated_at: datetime


class categoryitem(BaseModel):
    name:str
    descripiton: str    