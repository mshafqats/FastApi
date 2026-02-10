from fastapi import FastAPI
from app.public.router import router as public_router
from app.users.router import router as users_router
from app.api.ask import router as ask_router

app = FastAPI()
app.include_router(public_router)
app.include_router(users_router)
app.include_router(ask_router)
