import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

# Load variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

class DatabaseSession:
    def __init__(self, url: str = DATABASE_URL):
        self.engine = create_async_engine(url, echo=True)
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False
        )

    # close connection
    async def close(self):
        """Closes the database engine connection properly."""
        await self.engine.dispose()

    # Prepare the context for the asynchronous operation
    async def __aenter__(self) -> AsyncSession:
        self.session = self.SessionLocal()
        return self.session

    # used to clean up resources etc.
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def get_db(self) -> AsyncGenerator[AsyncSession, None]:
        async with self as db:
            yield db  # Ensures proper session cleanup

    async def commit_or_rollback(self):
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise


db = DatabaseSession()
Base = declarative_base()
