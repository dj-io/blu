from starlette import status
from uuid import UUID
from Model.user import User
from Resource.config import db
from Resource.schemas.user import UpdateRequest
from sqlalchemy.orm import joinedload
from sqlalchemy import update as sql_update, delete as sql_delete
from sqlalchemy.sql import select

class UserRepository:

    @staticmethod
    async def register(user_data: User):
        async with db as session:
            session.add(user_data)
            await db.commit_or_rollback()
            return status.HTTP_201_CREATED

    @staticmethod
    async def get_all():
        async with db as session:
            query = select(User).options(joinedload(User.generations))
            result = await session.execute(query)
            return result.unique().scalars().all()

    @staticmethod
    async def get_by_id(user_id: UUID):
        async with db as session:
            stmt = select(User).where(User.id == user_id).options(joinedload(User.generations))
            result = await session.execute(stmt)
            user = result.scalars().first()
            return user


    @staticmethod
    async def get_by_email(email: str):
        async with db as session:
            stmt = select(User).where(User.email == email)
            result = await session.execute(stmt)
            user = result.scalars().first()
            return user

    @staticmethod
    async def get_by_username(username: str):
        async with db as session:
            stmt = select(User).where(User.username == username).options(joinedload(User.generations))
            result = await session.execute(stmt)
            user = result.scalars().first()
            return user

    @staticmethod
    async def update(user_id: UUID, user_data: UpdateRequest):
        async with db as session:
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            user = result.scalars().first()

            query = sql_update(user).where(user.id == user_id).values(
                **user_data.model_dump(exclude_unset=True)).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()
            return status.HTTP_204_NO_CONTENT

    @staticmethod
    async def delete(user_id: UUID):
       async with db as session:
            query = sql_delete(User).where(User.id == user_id)
            await session.execute(query)
            await db.commit_or_rollback()
            return status.HTTP_200_OK
