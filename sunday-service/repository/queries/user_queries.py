import graphene
from security.auth import authenticate_request
from .schemas import user_schema
from resources.db_conn import db_session
from resources.models import user_model

db = db_session.session_factory()

class UserQuery(graphene.ObjectType):
    user_by_name = graphene.Field(user_schema.UserResponse, token=graphene.String(required=True))

    def resolve_user_by_name(self, info, token):
         user = authenticate_request(token)
         if user:
            return db.query(user_model.Users).filter_by(username=user.username).first()
