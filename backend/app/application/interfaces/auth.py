from abc import ABC, abstractmethod


class IPasswordHasher(ABC):
    @abstractmethod
    def hash_password(self, plain_password: str) -> str:
        pass

    @abstractmethod
    def verify_password(
        self,
        plain_password: str,
        hashed_password: str,
    ) -> str:
        pass


class ITokenProvider(ABC):
    @abstractmethod
    def generate_access_token(self, payload: dict) -> str:
        pass

    @abstractmethod
    def generate_refresh_token(self, payload: dict) -> str:
        pass

    @abstractmethod
    def decode_token(self, token: str) -> dict:
        pass
