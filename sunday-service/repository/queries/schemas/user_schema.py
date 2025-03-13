import graphene
from ..lib import types

class UserResponse(graphene.ObjectType):
    id = graphene.UUID()
    username = graphene.String()
    generations = graphene.List(types.UserGenerationsResponse)
