from fastapi import FastAPI
from krypt.auth_server.routers.auth.auth_router import auth_router
from krypt.auth_server.routers.user.user_router import user_router


app: FastAPI = FastAPI()


app.include_router(user_router)
app.include_router(auth_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"app": "krypt-auth-sever", "version": "1.0.0", "docs": "/docs"}
