import graphene
from sqlalchemy.orm import joinedload
from security.auth import authenticate_request
from .schemas import user_schema
from resources.db_conn import db_session
from resources.models import user_model

db = db_session.session_factory()

class UserQuery(graphene.ObjectType):
    retrieve_user = graphene.Field(user_schema.UserResponse, token=graphene.String(required=True))

    def resolve_retrieve_user(self, info, token):
         user = authenticate_request(token)
         if user:
            return db.query(user_model.User).options(joinedload(user_model.User.generations)).filter_by(username=user.username).first()
