from fastapi import FastAPI

from app.routers import admin, auth, manager, technician, user
from . import db, models

app = FastAPI()

db.Base.metadata.create_all(bind=db.engine)


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(manager.router)
app.include_router(admin.router)
app.include_router(technician.router)

@app.get("/")
def root():
    return {"msg": "Hello Naina"}
