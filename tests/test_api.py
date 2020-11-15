# pylint: disable=redefined-outer-name, missing-docstring
import sys
from uuid import uuid4, UUID
from os import unlink

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# TODO: During "pytest" runs the sys.path is incorrect and is unable to import
#       project files. This fixes that. It should not be necessary and further
#       investigation is needed.
sys.path.insert(0, "")

from melldechof.api import app, get_db
from melldechof.db import Base, User


def run_migrations(script_location: str, dsn: str) -> None:
    alembic_cfg = Config('alembic.ini')
    alembic_cfg.set_main_option('script_location', script_location)
    alembic_cfg.set_main_option('sqlalchemy.url', dsn)
    command.upgrade(alembic_cfg, 'head')


@pytest.fixture
def client():

    # TODO: Something was wonky with the environment when implementing this
    #       preventing me from using an in-memory DB for testing
    dsn = "sqlite:///./test.db"
    run_migrations("alembic", dsn)
    engine = create_engine(
        dsn, connect_args={"check_same_thread": False}
    )
    factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    test_session = factory()

    app.dependency_overrides[get_db] = lambda: test_session

    test_user = User(id=UUID('e9432395-603f-41ac-9fa3-0521d9cef9b8'), email="foo@bar.com")
    test_session.add(test_user)
    test_session.flush()

    yield TestClient(app)
    app.dependency_overrides = {}
    unlink("test.db")


@pytest.mark.dependency()
def test_store_new_presence(client):
    event_id = uuid4()
    user_id = "e9432395-603f-41ac-9fa3-0521d9cef9b8"
    response = client.put(f"/presence/{user_id}/{event_id}/present")
    assert response.status_code == 201, response.text
    assert response.json() == {"userId": str(user_id), "eventId": str(event_id), "presence": "present"}


@pytest.mark.dependency(depends=["test_store_new_presence"])
def test_update_presence(client):
    event_id = uuid4()
    user_id = "e9432395-603f-41ac-9fa3-0521d9cef9b8"
    client.put(f"/presence/{user_id}/{event_id}/present")
    response = client.put(f"/presence/{user_id}/{event_id}/present")
    assert response.status_code == 200, response.text
    assert response.json() == {"userId": str(user_id), "eventId": str(event_id), "presence": "present"}