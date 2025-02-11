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
