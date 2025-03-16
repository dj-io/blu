from pydantic import BaseModel
import uuid

class ContentGenRequest(BaseModel):
    content_type: str
    content_context: str
    user_context: str | None = None
    user_id: uuid.UUID

class GeneratedContentRequest(BaseModel):
    sections: dict[str, str]

class TikToken(BaseModel):
    _in: int
    _out: int
