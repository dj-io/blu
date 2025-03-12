import graphene
from security.auth import authenticate_request
from .schemas import generation_schema
from resources.db_conn import db_session
from resources.models import generation_model

db = db_session.session_factory()

class ContentQuery(graphene.ObjectType):
    all_content = graphene.List(generation_schema.ContentGenResponse, token=graphene.String(required=True))
    content_by_id = graphene.Field(generation_schema.ContentGenResponse, content_id=graphene.Int(required=True), token=graphene.String(required=True))

    def resolve_all_content(self, info, token):
         authenticated = authenticate_request(token)

         if authenticated:
            return db.query(generation_model.Generation).filter(generation_model.Generation.user_id == authenticated.id).all()

    def resolve_content_by_id(self, info, content_id, token):
         gen_model = generation_model.Generation
         authenticated = authenticate_request(token)

         if authenticated:
            return db.query(gen_model).filter(gen_model.user_id == authenticated.id, gen_model.id == content_id).first()
