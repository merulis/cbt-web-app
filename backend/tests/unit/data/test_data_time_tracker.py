import os
import pytest

from datetime import datetime

from app.models.time_tracker import ActivityRecord
from app.errors.db import Missing


os.environ["SQLITE_DB"] = ":memory:"
from app.data import time_tracker as data


@pytest.fixture
def sample() -> ActivityRecord:
    return ActivityRecord(
        id=1,
        color="green",
        type="work",
        interval=86400,
        date=datetime(year=2024, month=12, day=1),
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
    sample.color = "red"
    resp = data.modify(sample.id, sample)
    assert sample == resp


def test_modify_missing(sample):
    sample.color = "red"
    with pytest.raises(Missing):
        _ = data.modify(sample.id + 1, sample)


def test_delete():
    resp = data.delete(1)
    assert resp is True


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = data.delete(sample.id + 1)
