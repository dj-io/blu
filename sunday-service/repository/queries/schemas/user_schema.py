import graphene

class UserResponse(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()

