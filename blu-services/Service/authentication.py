import bcrypt
from Model.user import User
from Graphql.schema import LoginType
from Security.JWTManager import JWTManager
from Repository.user import UserRepository
from Resource.schemas.user import LoginRequest, RegisterRequest

class AuthenticationService:

    @staticmethod
    async def login(login_data: LoginRequest) -> LoginType | ValueError:
        existing_user = await UserRepository.get_by_username(login_data.username)

        if  bcrypt.checkpw(login_data.password.encode("utf-8"), existing_user.password.encode("utf-8")):
            token = JWTManager.create_access_token({"sub": login_data.username})
            return LoginType(token=token)
        else:
            raise ValueError("Incorrect username or password")

    @staticmethod
    async def register(user_data: RegisterRequest) -> str | ValueError:
        existing_user = await UserRepository.get_by_username(user_data.username)
        if existing_user:
            raise ValueError("Sorry this username is already taken!")

        hash_pw  = bcrypt.hashpw(user_data.password.encode("utf-8"), bcrypt.gensalt()) # hash user password
        hashed_pw = hash_pw.decode("utf-8")

        user = User()
        user.email = user_data.email
        user.username = user_data.username
        user.password = hashed_pw
        await UserRepository.register(user)

        return f'Successfully registered user as {user.username}'
