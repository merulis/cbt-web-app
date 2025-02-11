import pytest
from unittest.mock import Mock

from app.domain.entities.user import UserEntity
from app.application.use_cases.user_register import RegisterUserCase


@pytest.fixture
def example_user():
    return {
        "email": "test@test.com",
        "username": "test",
        "plain_password": "pw",
    }


def test_register_user_success(example_user):
    def save_side_effect(user: UserEntity):
        return user

    mock_repo = Mock()
    mock_hasher = Mock()

    mock_repo.get_by_email.return_value = None

    mock_repo.save.side_effect = save_side_effect

    mock_hasher.hash_password.return_value = "hashed_pass"

    register_user_case = RegisterUserCase(
        user_repo=mock_repo,
        hasher=mock_hasher,
    )

    result = register_user_case.execute(**example_user)

    mock_repo.get_by_email.assert_called_once_with(email="test@test.com")
    mock_hasher.hash_password.assert_called_once_with(
        plain_password="pw",
    )

    mock_repo.save.assert_called_once()

    assert result.email == "test@test.com"
    assert result.hashed_password == "hashed_pass"


def test_register_user_already_exists():
    mock_repo = Mock()
    mock_hasher = Mock()

    mock_repo.get_by_email.return_value = UserEntity(
        id=None,
        username="test",
        email="existing@example.com",
        hashed_password="somehash",
    )

    register_user_case = RegisterUserCase(
        user_repo=mock_repo,
        hasher=mock_hasher,
    )

    with pytest.raises(ValueError) as exc:
        register_user_case.execute(
            "test",
            "existing@example.com",
            "plain_password",
        )

    assert "already exists" in str(exc.value)

    mock_hasher.hash_password.assert_not_called()
    mock_repo.save.assert_not_called()
