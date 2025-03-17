import graphene
from resources.db_conn import db_session
from security.auth import authenticate_request
from resources.models import generation_model
from repository.mutations.schemas import generation_schema as mut_schema
from tools.ai import generate

db = db_session.session_factory()

class GenerateContent(graphene.Mutation):
    """Generate Documentation of any type i.e readme, design doc, changelog"""

    # set the arguments we want to accept in our mutation (request body)
    class Arguments:
        content_type = graphene.String()
        content_context = graphene.String()
        user_context = graphene.String()
        token = graphene.String(required=True)

    # define return data
    result = graphene.String()
    generated_content = graphene.JSONString()
    tokens = graphene.JSONString()

    @staticmethod
    async def mutate(root, info, content_type, content_context, user_context, token):

        authenticated = authenticate_request(token)

        if authenticated:
            generation_request = mut_schema.ContentGenRequest(
                content_type=content_type,
                content_context=content_context,
                user_context=user_context,
                user_id=authenticated.id
            )

            # generated_content, tokens = generative_utils.generate_docs(generation_request)
            generated_content, tokens = generate.generate_docs(generation_request)

            # prepare data to be added into the database
            db_content = generation_model.Generation(
                **generation_request.model_dump(),
                generated_content=generated_content,
                tokens=tokens
            )
            # db.add(db_content)
            # db.commit()
            # db.refresh(db_content)
            result = f"Successfully generated {generation_request.content_type} content"
            return GenerateContent(result=result, generated_content=db_content.generated_content, tokens=db_content.tokens)
