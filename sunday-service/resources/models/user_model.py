import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from resources.db_conn import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password =  Column(String(255))

    generations = relationship("Generation", back_populates="user")
