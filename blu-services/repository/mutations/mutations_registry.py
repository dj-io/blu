import graphene
from .content_mutations import GenerateContent
from .user_mutations import Register, Login

# Mutation Registry
class Mutations(graphene.ObjectType):

    # USER MUTATIONS
    register = Register.Field()
    login = Login.Field()

    # CONTENT MUTATIONS
    generate_content = GenerateContent.Field()
