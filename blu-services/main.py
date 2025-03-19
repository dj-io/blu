import uvicorn
import strawberry
from fastapi import FastAPI
from contextlib import asynccontextmanager
from Resource.config import db

from Graphql.queries.registry import Query
from Graphql.mutations.registry import Mutation

from strawberry.fastapi import GraphQLRouter
from alembic import command
from alembic.config import Config


def init_app():

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        print("🚀 BLU Services starting...")

        #  Check if Alembic migrations need to be applied
        # print("Checking Alembic migrations...")
        # alembic_cfg = Config("Resource/alembic.ini")  # Ensure the path is correct
        # command.upgrade(alembic_cfg, "head")  # Apply pending migrations
        yield # Everything before `yield` runs at startup, everything after runs at shutdown
        print("🛑 BLU Services shutting down... Closing DB connection...")
        await db.close()  # Closes DB connection

    app = FastAPI(
        title="blu",
        description="blu-services",
        version="0.1.0",
        lifespan=lifespan
    )

    @app.get("/")
    def home():
        return "Welcome home!"

    # add graphql endpoint
    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema)

    app.include_router(graphql_app, prefix="/graphql")
    return app


app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
