from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit,published:bool = False,sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} Published Blogs from the list'}
    else:
        return {'data':f'{limit} Blogs from the list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'All unpublished blogs'}

# '/' called as path
# get,post, delete  called as operation
#path operation decorator '@app'
@app.get('/blog/{id}')
#path operation function
def show(id:int):
    #fetch blog with id=id
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')
def createBlog(blog:Blog):
    return {'data':'Blog is created with title as 'f"{blog.title}"}
