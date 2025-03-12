from sqlalchemy import Column, Integer, String, UUID

from resources.db_conn import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password =  Column(String(255))
