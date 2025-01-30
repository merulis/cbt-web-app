from app.domain.repositories.user import IUserRepository
from app.application.interfaces.auth import IPasswordHasher
from app.application.interfaces.auth import ITokenProvider

from app.application.dto.jwt_payload import PayloadDTO


class LoginUserCase:
    def __init__(
        self,
        user_repo: IUserRepository,
        hasher: IPasswordHasher,
        token_provider: ITokenProvider,
    ):
        self.repo = user_repo
        self.hasher = hasher
        self.token_provider = token_provider

    def execute(self, email: str, plain_password: str) -> str:
        """
        return: tuple(access_token, refresh_token: str)
        """
        user = self.repo.get_by_email(email=email)
        if not user:
            raise ValueError("User not found or invalid credentials")

        if not self.hasher.verify_password(
            plain_password=plain_password,
            hashed_password=user.hashed_password,
        ):
            raise ValueError("Invalid credentials")

        if not user.is_active:
            raise ValueError("User is not active")

        payload = PayloadDTO(sub=str(user.id), role=user.role)

        access_token = self.token_provider.generate_access_token(
            payload=payload.to_dict(),
        )

        refresh_token = self.token_provider.generate_refresh_token(
            payload=payload.to_dict()
        )

        return (access_token, refresh_token)
