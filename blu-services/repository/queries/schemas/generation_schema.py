import graphene
from ..lib import types

class ContentGenResponse(graphene.ObjectType):
    id = graphene.ID()
    content_type = graphene.String()
    content = graphene.String()
    content_context = graphene.String()
    user_context = graphene.String()
    generated_content = graphene.JSONString()
    tokens = graphene.ObjectType()
    time_created = graphene.DateTime()
    time_updated = graphene.DateTime()
    user = graphene.Field(types.GenerationsUserResponse)
