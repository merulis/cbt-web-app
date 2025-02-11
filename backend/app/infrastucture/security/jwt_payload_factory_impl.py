from typing import Type

from app.infrastucture.security import IJWTPayloadFactory
from app.infrastucture.security.jwt_payload_scheme import JWTPayloadSchema


class JWTPayloadFactory(IJWTPayloadFactory):
    def __init__(
        self,
        access_payload_schema: Type[JWTPayloadSchema],
        refresh_payload_schema: Type[JWTPayloadSchema],
    ):
        self._access_payload_schema = access_payload_schema
        self._refresh_payload_schema = refresh_payload_schema

    def create_access_payload(self, data):
        payload = self._access_payload_schema(**data)
        return payload.to_dict()

    def create_refresh_payload(self, data):
        payload = self._refresh_payload_schema(**data)
        return payload.to_dict()
