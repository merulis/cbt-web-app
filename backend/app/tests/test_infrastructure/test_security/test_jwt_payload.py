from datetime import datetime, timedelta

from app.infrastucture.security.jwt_payload_scheme import (
    TokenType,
    BaseJWTPayload,
    AccessJWTPayload,
    RefreshJWTPayload,
)


def test_base_jwt_payload_to_dict():
    payload = BaseJWTPayload(sub="user123", role="admin")
    payload_dict = payload.to_dict()

    assert payload_dict["sub"] == "user123"
    assert payload_dict["role"] == "admin"

    assert isinstance(payload_dict["iat"], datetime)


def test_access_jwt_payload():
    payload = AccessJWTPayload(sub="user123", role="admin")
    payload_dict = payload.to_dict()

    assert payload_dict["jtt"] == TokenType.ACCESS

    assert payload.iat < payload.exp

    expected_exp = payload.iat + timedelta(minutes=1)
    assert abs((payload.exp - expected_exp).total_seconds()) < 1


def test_refresh_jwt_payload():
    payload = RefreshJWTPayload(sub="user123", role="admin")
    payload_dict = payload.to_dict()

    assert payload_dict["jtt"] == TokenType.REFRESH

    assert payload.iat < payload.exp

    expected_exp = payload.iat + timedelta(days=7)
    assert abs((payload.exp - expected_exp).total_seconds()) < 1
