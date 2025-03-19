import strawberry
from typing import List
from Security.JWTBearer import IsAuthenticated
from Service.user import UserService
from ..schema import UserType
from uuid import UUID

@strawberry.type
class UserQuery:

    @strawberry.field
    def hello_users(self) -> str:
        return "Hello Users!"

    @strawberry.field(permission_classes=[IsAuthenticated])
    async def get_all_users(self) -> list[UserType]:
        return await UserService.get_all()

    @strawberry.field(permission_classes=[IsAuthenticated])
    async def get_user_by_id(self, user_id: UUID) -> UserType:
        return await UserService.get_by_id(user_id)

    @strawberry.field(permission_classes=[IsAuthenticated])
    async def get_user_by_username(self, username: str) -> UserType:
        return await UserService.get_by_username(username)
