import bcrypt

from app.application.interfaces.auth import IPasswordHasher


class PasswordHasher(IPasswordHasher):
    def hash_password(self, plain_password):
        salt = bcrypt.gensalt()

        pw: bytes = plain_password.encode()
        return bcrypt.hashpw(password=pw, salt=salt)

    def verify_password(self, plain_password, hashed_password):
        return bcrypt.checkpw(
            password=plain_password.encode(),
            hashed_password=hashed_password,
        )
