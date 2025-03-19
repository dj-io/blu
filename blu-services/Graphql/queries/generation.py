import strawberry
from typing import List
from Security.JWTBearer import IsAuthenticated, IsAuthorized
from Service.generation import GenerationService
from ..schema import GenerationType
from uuid import UUID

@strawberry.type
class GenerationQuery:

    @strawberry.field
    def hello_generations(self) -> str:
        return "Hello Generations!"

    @strawberry.field(permission_classes=[IsAuthorized])
    async def get_all_generations(self, user_id: UUID) -> List[GenerationType]:
        return await GenerationService.get_all(user_id)

    @strawberry.field(permission_classes=[IsAuthorized])
    async def get_generation_by_id(self, generation_id: UUID, user_id: UUID) -> GenerationType:
        return await GenerationService.get_by_id(generation_id, user_id)
