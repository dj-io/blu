from pydantic import BaseModel
import uuid

class TikToken(BaseModel):
    _in: int
    _out: int

    class Config:
        from_attributes = True

class ContentGenRequest(BaseModel):
    content_type: str
    content_context: str
    user_id: uuid.UUID

    class Config:
        from_attributes = True

class UpdateContentGenRequest(BaseModel):
    content_context: str
    generated_content: dict[str, str]
    tokens: TikToken

    class Config:
        from_attributes = True

class GeneratedContentRequest(BaseModel):
    sections: dict[str, str]

