import pytest
from unittest.mock import Mock

from app.domain.entities.user import UserEntity
from app.application.use_cases.user_register import RegisterUserCase


def test_register_user_success():
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

    result = register_user_case.execute(
        email="test@example.com", plain_password="plain_password"
    )

    mock_repo.get_by_email.assert_called_once_with(email="test@example.com")
    mock_hasher.hash_password.assert_called_once_with(
        plain_password="plain_password",
    )

    mock_repo.save.assert_called_once()

    assert isinstance(result, UserEntity)
    assert result.email == "test@example.com"
    assert result.hashed_password == "hashed_pass"


def test_register_user_already_exists():
    mock_repo = Mock()
    mock_hasher = Mock()

    mock_repo.get_by_email.return_value = UserEntity(
        id=None, email="existing@example.com", hashed_password="somehash"
    )

    register_user_case = RegisterUserCase(
        user_repo=mock_repo,
        hasher=mock_hasher,
    )

    with pytest.raises(ValueError) as exc:
        register_user_case.execute("existing@example.com", "plain_password")

    assert "already exists" in str(exc.value)

    mock_hasher.hash_password.assert_not_called()
    mock_repo.save.assert_not_called()
