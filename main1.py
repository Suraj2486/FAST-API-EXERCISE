from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


class Post(BaseModel):
    name : str
    age : str
    published : bool = True
    rating : Optional[int] = None

app = FastAPI()

class LoanRequest:
    age : int
    income : float
    loan_amt : float
    exp_year : int

@app.get('/')
def get():
    return "Hello Naina"

@app.post('/post')
def post():
    return {"MSG" : "post successful"}

@app.post("/postjson")
def postjson(payload: dict = Body(...)):
    print(payload)
    return {"msg" : f"success postjson.. {payload["name"]}"}

@app.post("/condpost")
def condpost(new_post : Post):
    print(new_post)
    print(new_post.dict*())
    
