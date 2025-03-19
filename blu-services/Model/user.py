import uuid
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Resource.config import Base
from enum import Enum

class PlanEnum(str, Enum):
    HOBBY = "hobby"
    PRO = "pro"
    BUSINESS = "business"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password =  Column(String(255))
    active = Column(Boolean, default=False)
    plan = Column(String, default=PlanEnum.HOBBY)

    generations = relationship("Generation", back_populates="user")
