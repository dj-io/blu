import graphene
from .content_queries import ContentQuery
from .user_queries import UserQuery

# Query Registry
class Queries(
    ContentQuery,
    UserQuery,
    graphene.ObjectType
):
    pass
