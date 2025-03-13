import os
import jwt
from resources.models import user_model
from datetime import datetime, UTC
from security.key_generator_util import key_generator
from jwt import PyJWTError
from graphql import GraphQLError
from dotenv import load_dotenv
from resources.db_conn import db_session

load_dotenv(".env")

# bring in rsa keys
PRIVATE_KEY, PUBLIC_KEY = key_generator()

db = db_session.session_factory()

ALGORITHM = os.environ["ALGORITHM"]

def create_access_token(data, expires_delta):
    to_encode = data.copy()
    expire = datetime.now(UTC) + expires_delta
    to_encode.update({ "exp": expire })
    private_pem = PRIVATE_KEY.save_pkcs1().decode("utf-8")
    access_token = jwt.encode(to_encode, private_pem, algorithm=ALGORITHM)
    return access_token

def decode_access_token(data):
    public_pem = PUBLIC_KEY.save_pkcs1().decode("utf-8")
    token_data = jwt.decode(data, public_pem, algorithms=[ALGORITHM])
    return token_data

def authenticate_request(token):
    """
     call this in all requests that should only be executable with a valid token
    """

    try:
        payload = decode_access_token(data=token)
        username = payload.get("user")
        if username is None:
            raise GraphQLError("Corrupted payload")

    except PyJWTError:
        raise GraphQLError("Could not access credentials")

    user = db.query(user_model.User).filter(user_model.User.username == username).first()

    if user is None:
        raise GraphQLError("Invalid Credentials 3")

    return user
