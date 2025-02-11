import pytest

from app.infrastucture.security.password_hasher import PasswordHasher


@pytest.fixture
def hasher():
    return PasswordHasher()


def test_hash_return_bytes(hasher):
    pw = "password"
    hashed = hasher.hash_password(pw)

    assert isinstance(hashed, bytes)
    assert hashed != pw.encode()


def test_verify_pw_success(hasher):
    pw = "password"
    hashed = hasher.hash_password(pw)

    assert hasher.verify_password(pw, hashed) is True


def test_verify_pw_failure(hasher):
    pw = "password"
    pw_for_hash = "not_password"
    hashed = hasher.hash_password(pw_for_hash)

    assert hasher.verify_password(pw, hashed) is False


def test_hash_uniqueness(hasher):
    plain_password = "my_secret_password"
    hashed1 = hasher.hash_password(plain_password)
    hashed2 = hasher.hash_password(plain_password)

    assert hashed1 != hashed2
