import graphene
from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from repository.mutations import user_mutations, content_mutations
from repository.queries import content_queries, user_queries

app = Starlette()

# Merge queries (import from query dir)
class Query(
    content_queries.ContentQuery,
    user_queries.UserQuery,
    graphene.ObjectType
):
    pass

# Merge mutations (import from mutations dir)
class Mutation(
    user_mutations.UserMutations,
    content_mutations.ContentMutations,
    graphene.ObjectType
):
    pass

# Define GraphQL schema and pass full query and mutation args
app.mount(
    "/graphql",
    GraphQLApp(
        schema=graphene.Schema(
            query=Query,
            mutation=Mutation
            ),
            on_get=make_graphiql_handler() # runs the graphiql playground
    )
)
