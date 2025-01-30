import pytest

import uuid

from app.domain.entities.user import User


@pytest.fixture
def user():
    return User(
        id=uuid.uuid4(),
        email="example@example.com",
        hashed_password="random",
    )


def test_user_diactivate(user):
    user.deactivate()
    assert user.is_active is False


def test_user_activate(user):
    user.activate()
    assert user.is_active is True
