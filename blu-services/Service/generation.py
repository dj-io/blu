from Model.generation import Generation
from Graphql.schema import GenerationInput, GenerationType, GeneratedContentType
from Repository.generation import GenerationRepository
from Resource.schemas.generation import ContentGenRequest, UpdateContentGenRequest
from dataclasses import asdict
from uuid import UUID
from tools.ai import generate

class GenerationService:

    @staticmethod
    async def generate(generation_data: ContentGenRequest):
        generated_content, tokens = await generate.generate_docs(generation_data)
        generation = Generation(**asdict(generation_data), generated_content=generated_content, tokens=tokens)

        await GenerationRepository.generate(generation)
        return GeneratedContentType(sections=generated_content, tokens=tokens)

    @staticmethod
    async def get_all(user_id: UUID):
        list_generations = await GenerationRepository.get_all(user_id)
        return [GenerationType(
                id=generation.id,
                content_type=generation.content_type,
                content_context=generation.content_context,
                generated_content=generation.generated_content,
                tokens=generation.tokens,
                time_created=generation.time_created,
                time_updated=generation.time_updated,
                user=generation.user
            ) for generation in list_generations]

    @staticmethod
    async def get_by_id(generation_id: UUID, user_id: UUID):
        generation = await GenerationRepository.get_by_id(generation_id, user_id)
        return GenerationType(
                id=generation.id,
                content_type=generation.content_type,
                content_context=generation.content_context,
                generated_content=generation.generated_content,
                tokens=generation.tokens,
                time_created=generation.time_created,
                time_updated=generation.time_updated,
                user=generation.user
            )

    @staticmethod
    async def update(generation_id: UUID, generation_data: UpdateContentGenRequest):
        generated_content, tokens = await generate.generate_docs(generation_data)
        generation = Generation(**asdict(generation_data), generated_content=generated_content, tokens=tokens)

        await GenerationRepository.update(generation_id, generation)
        return GenerationType(**generation)

    @staticmethod
    async def delete(generation_id: UUID) -> str:
        await GenerationRepository.delete(generation_id)
        return f'Successfully deleted data by id {generation_id}'


