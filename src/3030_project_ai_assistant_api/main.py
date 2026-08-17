from fastapi import FastAPI
import chat_router

app = FastAPI()

app.include_router(chat_router.router)


