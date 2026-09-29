from app2 import schemas
from .db import client, session


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