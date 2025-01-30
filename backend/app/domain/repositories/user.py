from abc import ABC, abstractmethod

import uuid

from app.domain.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_by_uid(self, uid: uuid.UUID) -> User | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, uid: uuid.UUID) -> bool:
        pass
