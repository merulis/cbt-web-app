from app.models.user import NewUser, User
from app.data.database import (curs, IntegrityError)
from app.errors.db import Missing, Duplicate


curs.execute("""create table if not exists
             user(
                id integer primary key autoincrement,
                username text unique,
                email text,
                hash text
             )""")

curs.execute("""create table if not exists
             xuser(
                id integer primary key autoincrement,
                username text,
                email text,
                hash text
             )""")


def row_to_model(row: tuple) -> User:
    id, username, email, hash = row
    return User(id=id, username=username, email=email, hash=hash)


def model_to_dict(model: User) -> dict:
    return model.model_dump()


def get_one(id: int, table: str = "user") -> User:
    query = f"select * from {table} where id = :id"
    params = {"id": id}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(f"{table}: User {id} not found")


def get_all() -> list[User]:
    query = "select * from user"
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(user: NewUser, table: str = "user") -> User:
    query = f"""insert into {table} (username, email, hash)
            values (:username, :email, :hash)"""
    params = model_to_dict(user)
    try:
        curs.execute(query, params)
    except IntegrityError:
        raise Duplicate(msg=f"{table}: user {user.username} alredy exists")
    else:
        id_ = curs.lastrowid
        return get_one(id_, table)


def modify(id: int, user: NewUser) -> User:
    query = """update user
                set
                username=:username,
                email=:email,
                hash=:hash
                where id=:id"""
    params = model_to_dict(user)
    params["id"] = id
    curs.execute(query, params)
    if curs.rowcount == 1:
        return get_one(id)
    else:
        raise Missing(f"User {id} not found")


def delete(id_: int) -> bool:
    user = get_one(id_)
    query = "delete from user where id = :id"
    params = {"id": id_}
    resp = curs.execute(query, params)
    if curs.rowcount == 1:
        create(user, "xuser")
        return bool(resp)
    else:
        raise Missing(f"User {id_} not found")
