from typing import Union

from fastapi import FastAPI

from auth_server.routers.users import users
from auth_server.routers.auth import auth

app: FastAPI = FastAPI()


@app.get('/')
async def root() -> dict[str, str]:
    return {'app': 'krypt-auth-sever', 'version': '1.0.0', 'docs': '/docs'}

app.include_router(users, prefix='users')