from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas
from . import models
from .hashing import Hash
from .database import engine , get_db
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
from .routers import blog,user,authentication
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog', status_code=status.HTTP_201_CREATED,tags=['Blogs'])
# def create(request:schemas.Blog, db: Session=Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['Blogs'])
# def destroy(id,db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not found")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return {'Successfully Deleted'}

# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['Blogs'])
# def update(id,request:schemas.Blog,db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not found")
#     blog.update({'title':request.title,'body':request.body})
#     db.commit()
#     return {'Updated Successfully'}

# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['Blogs'])
# def allblog(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['Blogs'])
# def show(id,response:Response, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog wtih id {id} is not available.")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'deta*il':f"Blog wtih id {id} is not available."}
#     return blog



# @app.post('/user',response_model=schemas.ShowUser,tags=['Users'])
# def create_user(request:schemas.User,db:Session = Depends(get_db)):
#     new_user = models.User(name=request.name,email=request.email,password=Hash.bccrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=['Users'])
# def get_user(id:int,response:Response,db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User wtih id {id} is not available.")
#     return user
