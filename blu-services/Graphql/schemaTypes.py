import strawberry
from strawberry.scalars import JSON
from datetime import datetime
from uuid import UUID

@strawberry.type
class TokenCountType:
    _in: int
    _out: int

@strawberry.type
class SectionsType:
    pass

@strawberry.type
class UserGenerationsType:
    id: UUID
    content_type: str
    content_context: str
    generated_content: JSON
    tokens: TokenCountType
    time_created: datetime
    time_updated: datetime

@strawberry.type
class GenerationsUserType:
    id: UUID
    email: str
    username: str
    active: bool
    plan: str
