from fastapi import FastAPI
from krypt.auth_server.routers.auth import auth
from krypt.auth_server.routers.user import user


app: FastAPI = FastAPI()


app.include_router(user.user_router, prefix="/users")
app.include_router(auth.auth_router, prefix="/auth")


@app.get("/")
async def root() -> dict[str, str]:
    return {"app": "krypt-auth-sever", "version": "1.0.0", "docs": "/docs"}
