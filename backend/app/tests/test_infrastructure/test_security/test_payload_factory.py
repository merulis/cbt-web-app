import pytest

from app.infrastucture.security import JWTPayloadFactory


class TestAccessPayload:
    def __init__(self, sub):
        self.sub = sub
        self.type = "access"

    def to_dict(self) -> dict:
        return {"sub": self.sub, "type": self.type}


class TestRefreshPayload:
    def __init__(self, sub):
        self.sub = sub
        self.type = "refresh"

    def to_dict(self) -> dict:
        return {"sub": self.sub, "type": self.type}


@pytest.fixture
def factory():
    factory = JWTPayloadFactory(TestAccessPayload, TestRefreshPayload)
    return factory


def test_factory_access(factory):
    token = factory.create_access_payload({"sub": 1})

    assert isinstance(token, dict)
    assert token.get("sub") is not None
    assert token.get("sub") == 1


def test_factory_refresh(factory):
    token = factory.create_access_payload({"sub": 2})

    assert isinstance(token, dict)
    assert token.get("sub") is not None
    assert token.get("sub") == 2
