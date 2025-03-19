from uuid import UUID
from dataclasses import asdict
from Graphql.schema import UserType
from Model.user import User
from Repository.user import UserRepository
from Resource.schemas.user import UpdateRequest

class UserService:

    @staticmethod
    async def get_all():
        list_users = await UserRepository.get_all()
        return [UserType(
            id=user.id,
            username=user.username,
            active=user.active,
            plan=user.plan,
            generations=user.generations)
                for user in list_users]

    @staticmethod
    async def get_by_id(user_id: UUID):
        user = await UserRepository.get_by_id(user_id)
        return UserType(
            id=user.id,
            username=user.username,
            active=user.active,
            plan=user.plan,
            generations=user.generations)

    @staticmethod
    async def get_by_username(username: str):
        user = await UserRepository.get_by_username(username)
        return UserType(
            id=user.id,
            username=user.username,
            active=user.active,
            plan=user.plan,
            generations=user.generations)

    @staticmethod
    async def delete(user_id: UUID) -> str:
        await UserRepository.delete(user_id)
        return f'Successfully deleted data by id {user_id}'


    @staticmethod
    async def update(user_id: UUID, user_data: UpdateRequest) -> str:
        user = User(**asdict(user_data))
        await UserRepository.update(user_id, user)

        return f'Successfully updated data by id {user_id}'

