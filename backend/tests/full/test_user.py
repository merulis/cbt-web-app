import pytest
from fastapi.testclient import TestClient
from app.models.user import NewUser
from app.main import app


client = TestClient(app)
id_ = None


@pytest.fixture
def sample() -> NewUser:
    return NewUser(username="vadim", hash="123", email="123@123.com")


def test_create(sample):
    global id_
    resp = client.post("/user", json=sample.model_dump())
    id_ = resp.json().get("id")
    assert resp.status_code == 201


def test_create_duplicate(sample):
    resp = client.post("/user", json=sample.model_dump())
    assert resp.status_code == 409


def test_get_one(sample):
    resp = client.get(f"/user/{id_}").json()
    sample_ = sample.model_dump()
    sample_["id"] = id_
    assert resp == sample_


def test_get_one_missing():
    resp = client.get("/user/121414214")
    assert resp.status_code == 404


def test_modify(sample):
    sample.username = "newvadim"
    resp = client.patch(f"/user/{id_}", json=sample.model_dump())
    sample_ = sample.model_dump()
    sample_["id"] = id_
    assert resp.json() == sample_


def test_modify_missing(sample):
    resp = client.patch("/user/12412521521", json=sample.model_dump())
    assert resp.status_code == 404


def test_delete(sample):
    resp = client.delete(f"/user/{id_}")
    assert resp.json() is True
    assert resp.status_code == 200


def test_delete_missing(sample):
    resp = client.delete(f"/user/{id_}")
    assert resp.status_code == 404
