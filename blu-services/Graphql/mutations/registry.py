import strawberry
from .user import UserMutation
from .generation import GenerationMutation

@strawberry.type
class Mutation(UserMutation, GenerationMutation):
    pass
