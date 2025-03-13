import graphene

class UserGenerationsResponse(graphene.ObjectType):
    id = graphene.ID()
    content_type = graphene.String()
    content = graphene.String()
    content_context = graphene.String()
    user_context = graphene.String()
    generated_content = graphene.JSONString()
    time_created = graphene.DateTime()
    time_updated = graphene.DateTime()

class GenerationsUserResponse(graphene.ObjectType):
    id = graphene.UUID()
    username = graphene.String()
