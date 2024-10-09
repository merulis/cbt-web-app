from app.models.time_tracker import ActivityRecord


activies: list[ActivityRecord] = []


def get_all() -> list[ActivityRecord]:
    return activies


def get_one(id) -> ActivityRecord | None:
    for record in activies:
        if record.id == id:
            return record
    return None


def create(activity: ActivityRecord) -> ActivityRecord:
    activies.append(activity)
    return activity


def modify(id, activity: ActivityRecord) -> ActivityRecord:
    for record in activies:
        if record.id == id:
            activies.remove(record)
            activies.append(activity)
    return activity


def replace(id, activity: ActivityRecord) -> ActivityRecord:
    for record in activies:
        if record.id == id:
            activies.remove(record)
            activies.append(activity)
    return activity


def delete(id: int):
    for record in activies:
        if record.id == id:
            activies.remove(record)
            break
    return None
