import http

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

posts = [{'id':1, "name":"Naina", "age" : 20},
         {'id':2, "name":"Siyaa", "age" : 19}]

class Post(BaseModel):
    name : str
    age : int
    # published : bool = True
    # rating : Optional[int] = None

def find_by_id(id:int):
    for i,p in enumerate(posts):
        if p['id'] == id:
            return i

app = FastAPI()

j = 2
@app.get("/allposts")
def allposts():
    tpost = cursor.execute('''SELECT * FROM posts''')
    print(tpost)
    return {"posts" : posts}

@app.get("/post/{id:int}")
def postbyid(id:int, response : Response):
    post = None
    for p in posts:
        if p["id"] == id:
            post = p
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"{id} not found..")
        # response.status_code  = status.HTTP_404_NOT_FOUND
        # return f"{id} not found.."
    return post 

@app.post("/addpost", status_code = status.HTTP_201_CREATED)
def addpost(new_post : Post):
    global j
    p = {"id":j+1, "name":new_post.name, "age":new_post.age}
    j = j + 1
    posts.append(p)
    return posts


@app.delete('/deletepost/{id}')
def deletepost(id:int):
    post = find_by_id(id)
    if post is None:
        return "no post is thre"
    posts.pop(post)
    return {"msg":"deleted successfully"}

@app.put('/updatepost/{id}')
def updatepost(id:int, post:Post):
    index = int(find_by_id(id))
    print(index)
    if index is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"{id} not found..")
    temp_post = post.model_dump()
    print(temp_post)
    temp_post['id'] = id
    posts[index] = temp_post
    return posts