import strawberry
from ..schema import GenerationInput, GenerationType, GeneratedContentType, UpdateGenerationInput
from Security.JWTBearer import IsAuthenticated
from Service.generation import GenerationService
from Service.authentication import AuthenticationService
from uuid import UUID

@strawberry.type
class GenerationMutation:

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def generate(self, generation_data: GenerationInput) -> GeneratedContentType:
        return await GenerationService.generate(generation_data)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def update(self, generation_id: UUID, generation_data: UpdateGenerationInput) -> GenerationType:
        return await GenerationService.update(generation_id, generation_data)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def delete_generation(self, generation_id: UUID) -> str:
        return await GenerationService.delete(generation_id)
