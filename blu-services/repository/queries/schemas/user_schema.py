import graphene
from ..lib import types

class UserResponse(graphene.ObjectType):
    id = graphene.UUID()
    username = graphene.String()
    plan = graphene.String()
    active = graphene.Boolean()
    generations = graphene.List(types.UserGenerationsResponse)
