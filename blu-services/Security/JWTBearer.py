import typing

from strawberry.permission import BasePermission
from strawberry.types import Info
from .JWTManager import JWTManager


class IsAuthenticated(BasePermission):
    message = "User is not Authenticated!"

    async def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request = info.context["request"]

        # Access headers authentication
        authentication = request.headers["authentication"]

        if authentication:
            token = authentication.split("Bearer ")[-1]
            user = await JWTManager.verify_token(token)
            return user
        return False

class IsAuthorized(BasePermission):
    message = "User is not Authorized to take this action!"

    async def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request = info.context["request"]

        # get username or id from kwargs or source (args or data model instantiated on request)
        user_requested_name = kwargs.get("username") or (source.username if source else None)
        user_requested_id = kwargs.get("user_id") or (source.id if source else None)
        user_requested = user_requested_name if user_requested_id is None else user_requested_id

        # Access headers authentication
        authentication = request.headers["authentication"]

        if authentication:
            token = authentication.split("Bearer ")[-1]
            user_requesting = await JWTManager.verify_token(token)
            # if user_requested (id or name) in set of {id, username, generation user_id} return True else False
            return user_requested in { user_requesting.id, user_requesting.username }


        return False
