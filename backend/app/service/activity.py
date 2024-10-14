from app.data import time_tracker as db
from app.models.activity import Activity, ActivityBase


def get_all() -> list[Activity]:
    return db.get_all()


def get_one(id) -> Activity:
    return db.get_one(id)


def create(activity: ActivityBase) -> ActivityBase:
    return db.create(activity)


def modify(id: int, activity: ActivityBase) -> Activity:
    return db.modify(id, activity)


def replace(id: int, activity: ActivityBase) -> Activity:
    return db.replace(id, activity)


def delete(id: int) -> bool:
    return db.delete(id)
