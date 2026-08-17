import openai
from dotenv.main import load_dotenv
from openai import OpenAI


from chat_models import ChatRequest
import os

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
model: str = os.getenv("MODEL","")

client = OpenAI(api_key=key)

def generate_response(request : ChatRequest):
    try:
        response = client.responses.create(
            model = model,
            instructions="Respond like an insecure jealous/taunting girlfriend and keep the responses short.",
            input = request.userprompt
        )
        return response.output_text
    except openai.APITimeoutError:
        raise
    except openai.APIConnectionError:
        raise
    except openai.APIError:
        raise

