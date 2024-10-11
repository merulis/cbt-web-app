from .main import curs
from app.errors.db import Missing
from app.models.time_tracker import ActivityRecord, NewActivityRecord


curs.execute("""create table if not exists activies(
                id integer primary key autoincrement,
                color text,
                type text,
                interval integer,
                date text)""")


def row_to_model(row: tuple) -> ActivityRecord:
    id, color, type, interval, date = row
    return ActivityRecord(
        id=id,
        color=color,
        type=type,
        interval=interval,
        date=date
    )


def model_to_dict(model: ActivityRecord) -> dict:
    return model.model_dump()


def get_one(id: int) -> ActivityRecord:
    query = "select * from activies where id=:id"
    params = {"id": id}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(f"Activity {id} not found")


def get_all() -> list[ActivityRecord]:
    query = "select * from activies"
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(activity: NewActivityRecord) -> ActivityRecord:
    query = """insert into activies (color, type, interval, date)
            values (:color, :type, :interval, :date)"""
    params = model_to_dict(activity)
    curs.execute(query, params)
    id_ = curs.lastrowid
    return get_one(id_)


def modify(id: int, activity: NewActivityRecord) -> ActivityRecord:
    query = """update activies
                set color=:color,
                type=:type,
                interval=:interval,
                date=:date
                where id=:id"""
    params = model_to_dict(activity)
    params["id"] = id
    curs.execute(query, params)
    if curs.rowcount == 1:
        return get_one(id)
    else:
        raise Missing(f"Activity {id} not found")


def replace(id: int, activity: NewActivityRecord) -> ActivityRecord:
    query = """update activies
                set color=:color,
                type=:type,
                interval=:interval,
                date=:date
                where id=:id"""
    params = model_to_dict(activity)
    params["id"] = id
    curs.execute(query, params)
    if curs.rowcount == 1:
        return get_one(id)
    else:
        raise Missing(f"Activity {id} not found")


def delete(id: int) -> bool:
    query = "delete from activies where id = :id"
    params = {"id": id}
    resp = curs.execute(query, params)
    if curs.rowcount == 1:
        return bool(resp)
    else:
        raise Missing(f"Activity {id} not found")
