import jwt

from app.config import config
from app.application.interfaces.auth import ITokenProvider
from app.infrastucture.security import JWTPayloadFactory


class TokenProvider(ITokenProvider):
    def __init__(
        self,
        payload_factory: JWTPayloadFactory,
        public_key: str = config.JWT.PUBLIC_KEY.read_text(),
        private_key: str = config.JWT.PRIVATE_KEY.read_text(),
        algorithm: str = config.JWT.ALGORITHM,
    ):
        self._payload_factory = payload_factory
        self._public_key = public_key
        self._private_key = private_key
        self._algorithm = algorithm

    def _encode_token(
        self,
        payload: dict,
    ) -> str:
        encoded = jwt.encode(
            payload=payload,
            key=self._private_key,
            algorithm=self._algorithm,
        )
        return encoded

    def generate_access_token(self, data: dict) -> str:
        access_payload = self._payload_factory.create_access_payload(**data)
        token = self._encode_token(payload=access_payload.to_dict())
        return token

    def generate_refresh_token(self, data: dict) -> str:
        refresh_payload = self._payload_factory.create_refresh_payload(
            **data,
        )
        token = self._encode_token(payload=refresh_payload.to_dict())
        return token

    def decode_token(
        self,
        token: str | bytes,
    ) -> dict:
        decoded = jwt.decode(
            jwt=token,
            key=self._public_key,
            algorithms=[self._algorithm],
        )
        return decoded
