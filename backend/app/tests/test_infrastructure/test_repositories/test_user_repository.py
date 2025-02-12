import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.application.dto import UserDTO

from app.infrastucture.db import Base
from app.infrastucture.repositories_impl import UserRepositoryImpl


@pytest.fixture(scope="function")
def session():
    engine = create_engine("sqlite:///:memory:", echo=False)

    Base.metadata.create_all(engine)

    connection = engine.connect()
    transaction = connection.begin()

    Session = scoped_session(sessionmaker(bind=connection))
    session = Session()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def repo(session):
    return UserRepositoryImpl(session=session)


@pytest.fixture
def example_user():
    return UserDTO(
        username="test",
        email="test@email.com",
        hashed_password="12345",
    )


def test_save(repo, example_user):
    user_db = repo.save(example_user)

    assert user_db.id is not None
    assert user_db.role is not None
    assert user_db.created_at is not None

    assert isinstance(user_db.id, int)

    assert user_db.is_active is True

    assert user_db.hashed_password == example_user.hashed_password
    assert user_db.email == example_user.email


def test_get_by_uid(repo, example_user):
    saved = repo.save(example_user)
    retrieved = repo.get_by_uid(saved.id)
    assert retrieved is not None
    assert retrieved.email == example_user.email


def test_get_by_email(repo, example_user):
    saved = repo.save(example_user)
    retrieved = repo.get_by_email(example_user.email)
    assert retrieved is not None
    assert retrieved.id == saved.id


def test_update_user(repo, example_user):
    saved = repo.save(example_user)
    saved.email = "new@example.com"
    saved.hashed_password = "new_hashed_pass"
    updated = repo.update(saved)
    assert updated.email == "new@example.com"
    assert updated.hashed_password == "new_hashed_pass"


def test_delete_user(repo, example_user):
    saved = repo.save(example_user)
    repo.delete(saved.id)
    retrieved = repo.get_by_uid(saved.id)
    assert retrieved is None


def test_delete_non_existing(repo):
    with pytest.raises(ValueError):
        repo.delete(999)
