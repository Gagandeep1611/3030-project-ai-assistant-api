import openai
from dotenv.main import load_dotenv
from openai import OpenAI

import os

from app.chat_models import ChatRequest

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
model: str = os.getenv("MODEL","")

client = OpenAI(api_key=key)

def generate_response(request : ChatRequest):
    try:
        response = client.responses.create(
            model = model,
            instructions="Respond like an insecure jealous/taunting girlfriend and keep the responses short. and make sure you taunt",
            input = request.user_prompt
        )
        return response.output_text
    except openai.APITimeoutError:
        raise
    except openai.APIConnectionError:
        raise
    except openai.APIError:
        raise

