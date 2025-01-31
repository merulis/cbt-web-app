from abc import ABC, abstractmethod

import uuid

from app.domain.entities.user import UserEntity


class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_by_uid(self, uid: uuid.UUID) -> UserEntity | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity | None:
        pass

    @abstractmethod
    def update(self, user: UserEntity) -> UserEntity | None:
        pass

    @abstractmethod
    def delete(self, uid: uuid.UUID) -> None:
        pass
