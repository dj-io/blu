import os
import graphene
import bcrypt
from datetime import timedelta
from resources.models import user_model
from security.auth import create_access_token
from .schemas import user_schema
from resources.db_conn import db_session

db = db_session.session_factory()

class Register(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, email, username, password):
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()) # hash user password
        password_hash = hashed_password.decode("utf8") # ensures actual hash gets stored in database and not an encoded version of the hash

        user = user_schema.RegisterRequest(email=email, username=username, password=password_hash)
        db_user = user_model.Users(email=user.email, username=user.username, password=user.password)
        db.add(db_user)

        try:
            db.commit()
            db.refresh(db_user)
            db.close()
            return Register(ok=True)
        except:
            db.rollback()
            raise

class Token(graphene.ObjectType):
    access_token = graphene.String()
    token_type = graphene.String()

class Login(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()
    token = graphene.Field(Token)

    @staticmethod
    def mutate(root, info, username, password):
        # confirm data passed in to mutation matches the schema we set
        user = user_schema.LoginRequest(username=username, password=password)
        # confirm user exists by matching username
        db_user_info = db.query(user_model.Users).filter(user_model.Users.username == username).first()
        # if username exists we check the password passed in against the password of the user in db
        if bcrypt.checkpw(user.password.encode("utf-8"), db_user_info.password.encode("utf-8")):
            access_token_expires = timedelta(minutes=60)
            access_token = create_access_token(data={"user": username}, expires_delta=access_token_expires)
            ok = True
            return Login(ok=ok, token=Token(access_token=access_token, token_type="bearer"))
        else:
            ok = False
            return Login(ok=ok)

class UserMutations(graphene.ObjectType):
    register = Register.Field()
    login = Login.Field()
