from app.schemas.user import User, NewUser
from app.errors.exeptions import Missing, Duplicate


fakes = [
    User(id=1, username="kwijobo", email="123@qwe.com", hash="abc"),
    User(id=2, username="ermagerd", email="1123@qwe.com", hash="xyz"),
]


def find(id: int) -> User | None:
    for e in fakes:
        if e.id == id:
            return e
    return None


def check_missing(user: User):
    if user is None:
        raise Missing(msg=f"Missing user {id}")
    if not find(user.id):
        raise Missing(msg=f"Missing user {id}")


def check_duplicate(user: User):
    if find(user.id):
        raise Duplicate(msg=f"Duplicate user {id}")


def get_all() -> list[User]:
    return fakes


def get_one(id: int) -> User:
    user = find(id)
    check_missing(user)
    return user


def create(user: NewUser) -> User:
    check_duplicate(user)
    return user


def modify(id: int, user: NewUser) -> User:
    user = find(id)
    check_missing(user)
    return user


def delete(id: int) -> bool:
    user = find(id)
    check_missing(user)
    return True
