from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, JSON, UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from resources.db_conn import Base

class Generation(Base):
    __tablename__ = "generations"

    id = Column(UUID, primary_key=True, index=True)
    content_type = Column(String, index=True)
    content = Column(String)
    content_context = Column(String)
    user_context = Column(String)
    generated_content = Column(JSON)
    time_created = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    time_updated = Column(DateTime(timezone=True), onupdate=func.now(), index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True) # create manytoone relationship (user->generations)

    users = relationship("Users")
