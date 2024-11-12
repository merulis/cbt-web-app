from app.core import security as auth
from app.schemas.user import UserSchema


john = UserSchema(
    id=1,
    username="John",
    password=auth.hash_password("qwerty"),
    email="john@example.com",
    active=True,
)

sam = UserSchema(
    id=2,
    username="Sam",
    password=auth.hash_password("secret"),
    email="sam@example.com",
    active=True,
)

user_db: dict[str, UserSchema] = {
    john.username: john,
    sam.username: sam,
}
