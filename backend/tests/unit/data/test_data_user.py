import os
import pytest

from app.models.user import User
from app.errors.db import Missing


os.environ["SQLITE_DB"] = ":memory:"
from app.data import user as data


@pytest.fixture
def sample() -> User:
    return User(
        id=1,
        username="author",
        hash="qwerty",
        email="abc@abc.com"
    )


def test_create(sample):
    resp = data.create(sample)
    assert resp == sample


def test_get_one(sample):
    resp = data.get_one(sample.id)
    assert resp == sample


def test_get_one_missing(sample):
    with pytest.raises(Missing):
        _ = data.get_one(sample.id + 1)


def test_get_all(sample):
    resp = data.get_all()
    assert resp == [sample]


def test_modify(sample):
    sample.username = "red"
    resp = data.modify(sample.id, sample)
    assert sample == resp


def test_modify_missing(sample):
    sample.username = "red"
    with pytest.raises(Missing):
        _ = data.modify(sample.id + 1, sample)


def test_delete():
    resp = data.delete(1)
    assert resp is True


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = data.delete(sample.id + 1)
