from fastapi.testclient import TestClient
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

from tests.test_users import override_get_db


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:argusadmin@localhost/fastapiTest'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Testing_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




@pytest.fixture
def session():
    Base.metadata.create_all(bind=engine)
    Base.metadata.drop_all(bind=engine)
    db = Testing_SessionLocal()
    try:
        yield db
    finally:
        db.close()
    


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

# @pytest.fixture
# def client():
#     command.upgrade("head")
#     yield TestClient(app)
#     command.downgrade("base")