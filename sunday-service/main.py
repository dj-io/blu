import graphene
from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from repository.mutations import mutations_registry
from repository.queries import queries_registry


app = Starlette()

# Define GraphQL schema and pass full query and mutation args
app.mount(
    "/graphql",
    GraphQLApp(
        schema=graphene.Schema(
            query=queries_registry.Queries,
            mutation=mutations_registry.Mutations
            ),
            on_get=make_graphiql_handler() # runs the graphiql playground
    )
)
