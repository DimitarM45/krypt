from datetime import timedelta
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from krypt.auth_server.dependencies.services import get_auth_service, get_crypto_service, get_user_service
from krypt.auth_server.routers.auth.models.register_user_request import (
    RegisterUserRequest,
)
from krypt.configuration import Configuration
from krypt.services.abstract_auth_service import AbstractAuthService
from krypt.services.abstract_crypto_service import AbstractCryptoService
from krypt.services.abstract_user_service import AbstractUserService
from krypt.services.models.auth_user_dto import AuthUserDTO

from krypt.auth_server.routers.auth.models.token import Token

auth_router: APIRouter = APIRouter(prefix="/auth")

UserServiceDependency = Annotated[AbstractUserService, Depends(get_user_service)]
AuthServiceDependency = Annotated[AbstractAuthService, Depends(get_auth_service)]
CryptoServiceDependency = Annotated[AbstractCryptoService, Depends(get_crypto_service)]

@auth_router.post("/register", status_code=201)
async def register_user(
    request: RegisterUserRequest,
    user_service: UserServiceDependency,
):
    user_id: Optional[str] = await user_service.create_user(request)

    if not user_id:
        raise HTTPException(409, "User could not be created!")

    return user_id


@auth_router.post("/token", status_code=201, response_model=Token)
async def get_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    crypto_service: CryptoServiceDependency,
    auth_service: AuthServiceDependency,
    user_service: UserServiceDependency,
    config: Configuration = Depends(Configuration),
):
    user: Optional[AuthUserDTO] = await user_service.get_auth_user(form_data.username)

    credentials_exception = HTTPException(
        status_code=401,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if not user:
        raise credentials_exception

    is_password_correct: bool = crypto_service.verify_password_hash(
        form_data.password, user.password_hash
    )

    if not is_password_correct:
        raise credentials_exception

    access_token_data = {"sub": user.id}
    access_token_expiration: timedelta = timedelta(
        minutes=config.access_token_expiration_minutes
    )

    return auth_service.create_access_token(
        data=access_token_data,
        expires_delta=access_token_expiration,
        token_type="bearer",
    )


@auth_router.post("/logout")
async def logout_user():
    pass
