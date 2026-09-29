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
from . import models, schemas, utils

models.Base.metadata.create_all(bind = engine)


app = FastAPI()

@app.post("/adduser", status_code = status.HTTP_201_CREATED)
def addpost(new_post : schemas.User, db : Session = Depends(get_db)):

    user_dict = new_post.model_dump()
        
    hashed_pw = utils.hash(user_dict['pw'])
    user_dict['pw'] = hashed_pw
        
    temp = models.User(**user_dict)
    db.add(temp)
    db.commit()
    db.refresh(temp)
    return temp


@app.get('/user/{id}', response_model = schemas.Userout)
def getuser(id : int, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = f"id {id} not found")
    return user


