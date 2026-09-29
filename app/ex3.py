from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from app import schemas
from . import models
from .db import SessionLocal, engine, get_db
from sqlalchemy.orm import Session

from app import db

models.Base.metadata.create_all(bind = engine)


app = FastAPI()
while True:
    try:
        # conn = psycopg2.connect(host, database,username,password)
        conn = psycopg2.connect(host = 'localhost', database='fastapi',user='postgres',password='argusadmin', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("db connected")
        break
    except Exception as error:
        print("error in conn db : ", error)
        time.sleep(3)

# posts = [{'id':1, "name":"Naina", "age" : 20},
#          {'id':2, "name":"Siyaa", "age" : 19}]




app = FastAPI()

j = 2
@app.get("/allposts")
def allposts(db : Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data" : posts}



@app.get("/post/{id:int}")
def postbyid(id:int, db : Session = Depends(get_db)):
    tpost = db.query(models.Post).filter(models.Post.id == id).first()
    return {"posts" : tpost}

@app.post("/addpost", status_code = status.HTTP_201_CREATED,response_model=schemas.Post)
def addpost(new_post : schemas.PostBase, db : Session = Depends(get_db)):
    # print(new_post.model_dump())
    # temp = models.Post(name = new_post.name, age = new_post.age, published = new_post.published)
    temp = models.Post(**new_post.model_dump())
    db.add(temp)
    db.commit()
    db.refresh(temp)
    return temp

@app.delete('/deletepost/{id}')
def deletepost(id:int, db : Session = Depends(get_db)):
    tpost = db.query(models.Post).filter(models.Post.id == id).delete(synchronize_session = False)
    db.commit()
    return "deleted"

    
@app.put('/updatepost/{id}')
def updatepost(id:int, post:schemas.Post, db : Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    tpost = post_query.first()
    if tpost is None:
        return "no id"
    post_query.update(post.model_dump(), synchronize_session = False)
    db.commit()
    return post