from datetime import datetime, timedelta

from app.models.time_tracker import ActivityRecord
from app.service import time_tracker as service


record = ActivityRecord(
    id=1,
    color="green",
    type="work",
    interval=timedelta(days=1),
    date=datetime.now()
)

record_modify = ActivityRecord(
    id=1,
    color="red",
    type="work",
    interval=timedelta(days=1),
    date=datetime.now()
)


def test_create():
    resp = service.create(record)
    assert resp == record


def test_get_one():
    resp = service.get_one(1)
    assert resp == record


def test_get_all():
    resp = service.get_all()
    assert resp == [record]


def test_modify():
    resp = service.modify(1, record_modify)
    assert resp == record_modify


def test_replace():
    resp = service.replace(1, record_modify)
    assert resp == record_modify


def test_delete():
    resp = service.delete(1)
    assert resp is None
