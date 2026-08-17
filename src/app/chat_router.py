from fastapi import APIRouter
from chat_models import ChatRequest
import chat_service

router = APIRouter()

@router.post("/chat")
def chat_api(request: ChatRequest):
    return chat_service.generate_response(request)

