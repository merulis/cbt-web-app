import os
import pytest

from app.schemas.user import User, NewUser
from app.errors.exeptions import Missing


os.environ["SQLITE_DB"] = ":memory:"
from app.data import user as data


id_ = None


@pytest.fixture
def sample() -> NewUser:
    return NewUser(username="author", hash="qwerty", email="abc@abc.com")


def test_create(sample):
    global id_
    resp = data.create(sample)
    id_ = resp.id
    assert isinstance(resp, User)


def test_get_one(sample):
    resp = data.get_one(id_)
    assert isinstance(resp, User)


def test_get_one_missing(sample):
    with pytest.raises(Missing):
        _ = data.get_one(123124125)


def test_get_all(sample):
    resp = data.get_all()
    assert all(isinstance(item, User) for item in resp)


def test_modify(sample):
    sample.username = "red"
    resp = data.modify(id_, sample)
    assert isinstance(resp, User)
    assert resp.username == "red"


def test_modify_missing(sample):
    with pytest.raises(Missing):
        _ = data.modify(1241242145, sample)


def test_delete():
    resp = data.delete(id_)
    assert resp is True


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = data.delete(1241242145)
