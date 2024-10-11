from fastapi import HTTPException
import pytest
import os

os.environ["UNIT_TEST"] = "true"

from app.models.user import User, NewUser
from app.api.routes import user
from app.errors.db import Missing, Duplicate


@pytest.fixture
def sample() -> User:
    return User(id=3, email="avv@abb.com", username="Pa Tuohy", hash="...",)


@pytest.fixture
def fakes() -> list[User]:
    return user.get_all()


def assert_duplicate(exc):
    assert exc.value.status_code == 404
    assert "Duplicate" in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "Missing" in exc.value.msg


def test_create(sample):
    assert user.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        _ = user.create(fakes[0])
        assert_duplicate(exc)


def test_get_one(fakes):
    assert user.get_one(fakes[0].id) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        _ = user.get_one(5)
        assert_missing(exc)


def test_modify(fakes):
    assert user.modify(fakes[0].id, fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        _ = user.modify(sample.id, sample)
        assert_missing(exc)


def test_delete(fakes):
    assert user.delete(fakes[0].id) is True


def test_delete_missing(sample):
    with pytest.raises(HTTPException) as exc:
        _ = user.delete(4)
        assert_missing(exc)
