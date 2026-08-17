from pydantic import BaseModel


class ChatRequest(BaseModel):
    userprompt: str