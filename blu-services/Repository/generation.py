from starlette import status
from uuid import UUID
from sqlalchemy import update as sql_update, delete as sql_delete
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import select
from Resource.config import db
from Resource.schemas.generation import ContentGenRequest, UpdateContentGenRequest
from Model.generation import Generation

class GenerationRepository:

    @staticmethod
    async def generate(generation_data: ContentGenRequest):
        async with db as session:
            session.add(generation_data)
            await db.commit_or_rollback()
            return status.HTTP_201_CREATED

    @staticmethod
    async def get_all(user_id: UUID):
        async with db as session:
            query = select(Generation).where(Generation.user_id == user_id).options(joinedload(Generation.user))
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_by_id(generation_id: UUID, user_id: UUID):
        async with db as session:
            stmt = select(Generation).where(Generation.id == generation_id, Generation.user_id == user_id).options(joinedload(Generation.user))
            result = await session.execute(stmt)
            return result.scalars().first()

    @staticmethod
    async def update(generation_id: UUID, generation_data: UpdateContentGenRequest):
        async with db as session:
            stmt = select(Generation).where(Generation.id == generation_id)
            result = await session.execute(stmt)
            generation = result.scalars().first()

            query = sql_update(generation).where(generation.id == generation_id).values(
                **generation_data.model_dump(exclude_unset=True)).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()
            return status.HTTP_204_NO_CONTENT

    @staticmethod
    async def delete(generation_id: UUID):
        async with db as session:
            query = sql_delete(Generation).where(Generation.id == generation_id)
            await session.execute(query)
            await db.commit_or_rollback()
            return status.HTTP_200_OK
