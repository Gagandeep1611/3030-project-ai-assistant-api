from fastapi import FastAPI

from app import chat_router

app = FastAPI()

app.include_router(chat_router.router)


