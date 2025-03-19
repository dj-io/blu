import strawberry
from ..schema import UserInput, LoginInput, LoginType
from Security.JWTBearer import IsAuthenticated, IsAuthorized
from Service.user import UserService
from Service.authentication import AuthenticationService
from uuid import UUID

@strawberry.type
class UserMutation:

    @strawberry.mutation
    async def login(self, login_data: LoginInput) -> LoginType:
        return await AuthenticationService.login(login_data)

    @strawberry.mutation
    async def register(self, user_data: UserInput) -> str:
        return await AuthenticationService.register(user_data)

    @strawberry.mutation(permission_classes=[IsAuthorized])
    async def delete_user(self, user_id: UUID) -> str:
        return await UserService.delete(user_id)

    @strawberry.mutation(permission_classes=[IsAuthorized])
    async def update_user(self, user_id: UUID,  user_data: UserInput) -> str:
        return await UserService.update(user_id, user_data)
