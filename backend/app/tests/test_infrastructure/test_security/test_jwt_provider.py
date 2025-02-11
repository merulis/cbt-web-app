import pytest

import jwt

from app.infrastucture.security.jwt_provider import TokenProvider


class MockPayload:
    def __init__(self, **data):
        self.data = data

    def to_dict(self):
        return self.data


class MockFactory:
    def create_access_payload(self, **data):
        payload = MockPayload(**data)
        return payload

    def create_refresh_payload(self, **data):
        payload = MockPayload(**data)
        return payload


@pytest.fixture
def factory():
    return MockFactory()


@pytest.fixture
def provider(factory):
    return TokenProvider(
        payload_factory=factory,
        public_key="secret",
        private_key="secret",
        algorithm="HS256",
    )


def test_generate_access_token(provider):
    data = {"sub": "user123", "role": "admin"}
    token = provider.generate_access_token(data)

    assert isinstance(token, str)
    decoded = jwt.decode(token, key="secret", algorithms=["HS256"])
    for key, value in data.items():
        assert decoded.get(key) == value


def test_generate_refresh_token(provider):
    data = {"sub": "user456", "role": "user"}
    token = provider.generate_refresh_token(data)

    assert isinstance(token, str)
    decoded = jwt.decode(token, key="secret", algorithms=["HS256"])
    for key, value in data.items():
        assert decoded.get(key) == value


def test_decode_token(provider):
    data = {"sub": "user789", "role": "guest"}
    token = provider.generate_access_token(data)
    decoded = provider.decode_token(token)
    for key, value in data.items():
        assert decoded.get(key) == value


def test_decode_invalid_token(provider):
    invalid_token = "invalid.token.string"
    with pytest.raises(jwt.exceptions.InvalidTokenError):
        provider.decode_token(invalid_token)
