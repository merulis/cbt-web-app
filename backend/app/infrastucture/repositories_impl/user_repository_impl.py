from app.domain.repositories.user import IUserRepository


class UserRepositoryImpl(IUserRepository):
    def save(self, user):
        return None

    def get_by_uid(self, uid):
        return None

    def get_by_email(self, email):
        return None

    def update(self, user):
        return None

    def delete(self, uid):
        return None
