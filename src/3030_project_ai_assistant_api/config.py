import os

import openai
from dotenv.main import load_dotenv
from openai import OpenAI

load_dotenv()

async def get_openai_client():
        key = os.getenv("OPENAI_API_KEY")
        client = OpenAI(api_key = key)
        return client