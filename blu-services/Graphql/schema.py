from typing import Optional
import strawberry
from strawberry.scalars import JSON
from typing import List
from uuid import UUID
from enum import Enum
from datetime import datetime
from .schemaTypes import UserGenerationsType, GenerationsUserType

@strawberry.enum
class Plan(Enum):
    HOBBY = "hobby"
    PRO = "pro"
    BUSINESS = "business"

@strawberry.type
class LoginType:
    token: str
    token_type: str | None = "Bearer"

@strawberry.input
class LoginInput:
    username: str
    password: str

@strawberry.type
class UserType:
    id: UUID
    username: str
    active: bool
    plan: Plan
    generations: List[UserGenerationsType]

@strawberry.input
class UserInput:
    email: str | None = None
    username: str | None = None
    password: str | None = None


@strawberry.input
class TikTokenInput:
    _in: int
    _out: int

@strawberry.type
class GenerationType:
    id: UUID
    content_type: str
    content_context: str
    generated_content: JSON
    tokens: JSON
    time_created: datetime
    time_updated: datetime
    user: GenerationsUserType

@strawberry.input
class GenerationInput:
    content_type: str
    content_context: str
    user_id: UUID

@strawberry.input
class UpdateGenerationInput:
    content_context: str
    generated_content: JSON
    tokens: TikTokenInput

@strawberry.type
class GeneratedContentType:
    sections: JSON
    tokens: JSON

@strawberry.input
class GeneratedContentInput:
    sections: JSON
    tokens: JSON



