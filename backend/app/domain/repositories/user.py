from abc import ABC, abstractmethod

from app.application.dto import UserDTO

from app.domain.entities.user import UserEntity


class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: UserDTO) -> UserEntity:
        pass

    @abstractmethod
    def get_by_uid(self, uid: int) -> UserEntity | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity | None:
        pass

    @abstractmethod
    def update(self, user: UserEntity) -> UserEntity | None:
        pass

    @abstractmethod
    def delete(self, uid: int) -> None:
        pass
