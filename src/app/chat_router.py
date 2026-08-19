from fastapi import APIRouter

from app import chat_service
from app.chat_models import ChatRequest

router = APIRouter()

@router.post("/chat")
def chat_api(request: ChatRequest):
    return chat_service.generate_response(request)

