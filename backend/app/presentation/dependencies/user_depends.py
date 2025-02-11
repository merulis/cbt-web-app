from app.infrastucture.repositories_impl import UserRepositoryImpl
from app.infrastucture.db import sync_db
from app.infrastucture.security import (
    PasswordHasher,
    JWTPayloadFactory,
    TokenProvider,
    AccessJWTPayload,
    RefreshJWTPayload,
)


def get_user_repo():
    return UserRepositoryImpl(
        session=sync_db.get_session(),
    )


def get_password_hasher():
    return PasswordHasher()


def get_token_provider():
    payload_factory = JWTPayloadFactory(
        access_payload_schema=AccessJWTPayload,
        refresh_payload_schema=RefreshJWTPayload,
    )
    return TokenProvider(
        payload_factory=payload_factory,
    )
