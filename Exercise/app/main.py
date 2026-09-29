from fastapi import FastAPI
import time

from . import models, db
from .routers import auth, tickets, users
from .config import settings

from fastapi.middleware.cors import CORSMiddleware
from .db import Base

Base.metadata.create_all(bind=db.engine)


app = FastAPI()



# app.include_router(auth.router)
# app.include_router(tickets.router)
# app.include_router(users.router)

@app.get("/")
def root():
    return{"msg":"Hello Naina"}