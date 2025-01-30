import uuid

from app.domain.entities.user import User
from app.domain.repositories.user import IUserRepository


class GetUserCase:
    def __init__(self, user_repo: IUserRepository):
        self.repo = user_repo

    def execute(self, uid: uuid.UUID) -> User | None:
        return self.repo.get_by_uid(uid=uid)
