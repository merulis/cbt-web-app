from abc import ABC, abstractmethod


class IJWTPayloadFactory(ABC):
    @abstractmethod
    def create_access_payload(self, data: dict) -> dict:
        pass

    @abstractmethod
    def create_refresh_payload(self, data: dict) -> dict:
        pass
