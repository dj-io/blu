import strawberry
from .user import UserQuery
from .generation import GenerationQuery

# Query Registry
@strawberry.type
class Query(
    UserQuery,
    GenerationQuery
):
    pass
