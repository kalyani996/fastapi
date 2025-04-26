from typing import List
from pydantic import BaseModel

class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    class config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str
    class config():
        orm_mode = True

class ShowUser(User):
    name:str
    email:str
    blogs:List[Blog]
    class config():
        orm_mode = True

class ShowBlog(Blog):
    title:str
    creator: ShowUser
    class config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
