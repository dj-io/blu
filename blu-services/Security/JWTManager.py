import os
import jwt
from typing import Optional
from jwt import PyJWTError
from graphql import GraphQLError
from dotenv import load_dotenv
from datetime import datetime,timedelta, UTC
from Repository.user import UserRepository
from .key_generator_util import key_generator

load_dotenv(".env")

# bring in rsa keys
PRIVATE_KEY, PUBLIC_KEY = key_generator()

ALGORITHM = os.environ["ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]

class JWTManager:

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta]=timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES))):
        to_encode = data.copy()
        expire = datetime.now(UTC) + expires_delta
        to_encode.update({ "exp": expire })
        private_pem = PRIVATE_KEY.save_pkcs1().decode("utf-8")
        access_token = jwt.encode(to_encode, private_pem, algorithm=ALGORITHM)
        return access_token

    @staticmethod
    def decode_access_token(data):
        public_pem = PUBLIC_KEY.save_pkcs1().decode("utf-8")
        token_data = jwt.decode(data, public_pem, algorithms=[ALGORITHM])
        return token_data

    @staticmethod
    async def verify_token(token: str):
        """
        call this in all requests that should only be executable with a valid token
        """
        # verify JWT
        try:
            payload = JWTManager.decode_access_token(data=token)
            current_timestamp = datetime.now(UTC).timestamp()
            username = payload.get("sub")

            if username is None:
                raise GraphQLError("Corrupted payload")
            elif payload["exp"] <= current_timestamp:
                raise GraphQLError("Token expired!")

        except PyJWTError:
            raise GraphQLError("Could not access credentials")
        finally:
            # process user in payload
            user = await UserRepository.get_by_username(username)
            if user is None:
                raise GraphQLError("Altered Payload!")

            return user

