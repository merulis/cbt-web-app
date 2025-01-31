import uuid

from app.domain.entities.user import UserEntity
from app.domain.repositories.user import IUserRepository
from app.application.interfaces.auth import IPasswordHasher


class RegisterUserCase:
    def __init__(self, user_repo: IUserRepository, hasher: IPasswordHasher):
        self.repo = user_repo
        self.hasher = hasher

    def execute(self, email: str, plain_password: str) -> UserEntity:
        existing_user = self.repo.get_by_email(email=email)
        if existing_user is not None:
            raise ValueError("User with given email already exists")

        hashed_pw = self.hasher.hash_password(plain_password=plain_password)

        user = UserEntity(
            id=uuid.uuid4(),
            email=email,
            hashed_password=hashed_pw,
        )

        user_created = self.repo.save(user)

        return user_created
