from pydantic import BaseModel

class ContentGenRequest(BaseModel):
    content_type: str
    content: str
    content_context: str
    user_context: str | None = None
    user_id: int

class GeneratedContentRequest(BaseModel):
    sections: dict | None = None
