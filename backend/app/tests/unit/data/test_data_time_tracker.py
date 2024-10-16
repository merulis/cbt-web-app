import os
import pytest

from datetime import datetime

from app.schemas.activity import Activity, ActivityCreate
from app.errors.exeptions import Missing


os.environ["SQLITE_DB"] = ":memory:"
from app.data import time_tracker as data


id_ = None


@pytest.fixture
def sample() -> ActivityCreate:
    return ActivityCreate(
        color="green",
        category="work",
        interval=86400,
        date=datetime(year=2024, month=12, day=1),
    )


def test_create(sample):
    global id_
    resp = data.create(sample)
    id_ = resp.id
    assert isinstance(resp, Activity)


def test_get_one(sample):
    resp = data.get_one(id_)
    assert isinstance(resp, Activity)


def test_get_one_missing(sample):
    with pytest.raises(Missing):
        _ = data.get_one(1231245412)


def test_get_all(sample):
    resp = data.get_all()
    assert all(isinstance(item, Activity) for item in resp)


def test_modify(sample):
    sample.color = "red"
    resp = data.modify(id_, sample)
    assert isinstance(resp, Activity)
    assert resp.color == "red"


def test_modify_missing(sample):
    sample.color = "red"
    with pytest.raises(Missing):
        _ = data.modify(123124, sample)


def test_delete():
    resp = data.delete(id_)
    assert resp is True


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = data.delete(1241245215)
