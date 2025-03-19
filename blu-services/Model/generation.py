import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from Resource.config import Base

class Generation(Base):
    __tablename__ = "generations"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    content_type = Column(String, index=True)
    content_context = Column(String)
    user_context = Column(String)
    generated_content = Column(JSON)
    tokens = Column(JSON)
    time_created = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    time_updated = Column(DateTime(timezone=True), onupdate=func.now(), index=True)
    user_id = Column(UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)

    user = relationship("User", back_populates="generations")
