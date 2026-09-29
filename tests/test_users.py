from fastapi.testclient import TestClient
from app2 import schemas
import pytest

from app2.main import app
from app2.schemas import UserOut

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app2.config import settings
from app2.db import get_db
from app2.db import Base
from alembic import command


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:argusadmin@localhost/fastapiTest'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Testing_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = Testing_SessionLocal()
    try:
        yield db
    finally:
        db.close()



app.dependency_overrides[get_db] = override_get_db





@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    # run our code before we run our test
    yield TestClient(app)

    # run our code after out test finishes
    Base.metadata.drop_all(bind=engine)

# @pytest.fixture
# def client():
#     command.upgrade("head")
#     yield TestClient(app)
#     command.downgrade("base")



def test_root(client):
    res = client.get("/")
    print(res.json().get("msg"))
    assert res.json().get("msg") == "Hello Naina"
    assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json = {"email":"n@g.c", "password":"123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "n@g.c"
    assert res.status_code == 201