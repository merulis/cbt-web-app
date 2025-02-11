from sqlalchemy.orm import Session
from sqlalchemy import (
    select,
    update as sql_update,
)

from app.domain.entities.user import UserEntity
from app.domain.repositories.user import IUserRepository

from app.infrastucture.models import UserModel


class UserRepositoryImpl(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, user):
        with self.session as db:
            user_db = UserModel(**user.to_dict())
            db.add(user_db)
            db.commit()
            db.refresh(user_db)
            return self._to_entity(user_db)

    def get_by_uid(self, uid):
        with self.session as db:
            user_db = db.get(UserModel, uid)
            return self._to_entity(user_db) if user_db else None

    def get_by_email(self, email):
        stmt = select(UserModel).where(UserModel.email == email)
        with self.session as db:
            user_db = db.execute(stmt).scalar_one_or_none()
            return self._to_entity(user_db) if user_db else None

    def update(self, user):
        stmt = (
            sql_update(UserModel)
            .where(UserModel.id == user.id)
            .values(
                email=user.email,
                hashed_password=user.hashed_password,
                is_active=user.is_active,
                role=user.role,
            )
        )
        with self.session as db:
            _ = db.execute(stmt)
            db.commit()
            user_db = db.get(UserModel, user.id)
            if user_db:
                return self._to_entity(user_db)
            return None

    def delete(self, uid):
        with self.session as db:
            user_db = db.get(UserModel, uid)

            if not user_db:
                raise ValueError("User not found")

            db.delete(user_db)
            db.commit()

    def _to_entity(self, user_db: UserModel) -> UserEntity:
        return UserEntity(
            id=user_db.id,
            username=user_db.username,
            email=user_db.email,
            hashed_password=user_db.hashed_password,
            is_active=user_db.is_active,
            created_at=user_db.created_at,
            role=user_db.role,
        )
