import http
from tkinter import NE

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time

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

class Post(BaseModel):
    name : str
    age : int
    # published : bool = True
    # rating : Optional[int] = None

# def find_by_id(id:int):
#     for i,p in enumerate(posts):
#         if p['id'] == id:
#             return i

app = FastAPI()

j = 2
@app.get("/allposts")
def allposts():
    cursor.execute('''SELECT * FROM posts''')
    tpost = cursor.fetchall()
    print(tpost)
    return {"posts" : tpost}

@app.get("/post/{id:int}")
def postbyid(id:int, response : Response):
    cursor.execute("SELECT * FROM posts WHERE id = %s;", (id,))
    tpost = cursor.fetchone()
    print(tpost)
    return {"posts" : tpost}

@app.post("/addpost", status_code = status.HTTP_201_CREATED)
def addpost(new_post : Post):
    cursor.execute( "INSERT INTO posts (name, age) VALUES (%s, %s) RETURNING *", (new_post.name, new_post.age))
    temp = cursor.fetchone()
    conn.commit()
    return {"msg" : temp}

@app.delete('/deletepost/{id}')
def deletepost(id:int):
    cursor.execute('''DELETE FROM posts WHERE posts.id = %s''', (id,))
    conn.commit()
    return {"msg":"deleted successfully"}

@app.put('/updatepost/{id}')
def updatepost(id:int, post:Post):
    cursor.execute("UPDATE posts SET name = %s, age = %s WHERE posts.id = %s RETURNING *",(post.name,post.age,id))
    conn.commit()
    temp = cursor.fetchone()
    return {"msg": temp}