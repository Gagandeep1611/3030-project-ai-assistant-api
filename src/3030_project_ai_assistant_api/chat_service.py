from dotenv.main import load_dotenv

from config import get_openai_client
from model import ChatRequest
client = get_openai_client()
import os

load_dotenv()

def generate_response(request : ChatRequest):
    response = client.responses.create(
        model = os.getenv("MODEL"),
        input = request.question
    )
    return response.output_text
