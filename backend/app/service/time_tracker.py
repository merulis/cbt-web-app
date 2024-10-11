from app.data import time_tracker as db
from app.models.time_tracker import ActivityRecord, NewActivityRecord


def get_all() -> list[ActivityRecord]:
    return db.get_all()


def get_one(id) -> ActivityRecord:
    return db.get_one(id)


def create(activity: NewActivityRecord) -> NewActivityRecord:
    return db.create(activity)


def modify(id: int, activity: NewActivityRecord) -> ActivityRecord:
    return db.modify(id, activity)


def replace(id: int, activity: NewActivityRecord) -> ActivityRecord:
    return db.replace(id, activity)


def delete(id: int) -> bool:
    return db.delete(id)
