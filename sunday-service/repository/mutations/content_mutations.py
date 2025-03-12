import graphene
from resources.db_conn import db_session
from security.auth import authenticate_request
from resources.models import generation_model
from repository.mutations.schemas import generation_schema as mut_schema
from tools.ai import content_generator

db = db_session.session_factory()


class GenerateContent(graphene.Mutation):
    """Generate Documentation of any type i.e readme, design doc, changelog"""
    class Arguments: # set the arguments we want to accept in our mutation (request body)
        content_type = graphene.String()
        content = graphene.String()
        content_context = graphene.String()
        user_context = graphene.String()
        token = graphene.String(required=True)

    result = graphene.String()
    sections = graphene.JSONString()

    @staticmethod
    async def mutate(root, info, content_type, content, content_context, user_context, token):

        authenticated = authenticate_request(token)

        if authenticated:
            generation_request = mut_schema.ContentGenRequest(content_type=content_type, content=content, content_context=content_context, user_context=user_context, user_id=authenticated.id) # confirm data passed in matches what we expect in our schema
            generated_content = content_generator.generate_docs() # pass openai util function here (this will return a dict of the sections and content i.e {"section_name_one": "this is the generated content", "section_name_two": "this is the next sections generated content"})
            db_content = generation_model.Generation(**generation_request.model_dump(), generated_content=generated_content) # prepare data to be added into the database
            db.add(db_content)
            db.commit()
            db.refresh(db_content)
            result = f"Successfully generated {generation_request.content_type} content"
            return GenerateContent(result=result, sections=db_content.generated_content)


class ContentMutations(graphene.ObjectType):
   generate_content = GenerateContent.Field()
