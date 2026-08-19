# AI Text Assistant API

A beginner AI engineering project that demonstrates how to build an **LLM-powered backend API** using FastAPI and OpenAI.

The project focuses on understanding the fundamentals of integrating an LLM into a backend application, including **developer instructions, API integration, structured responses, and streaming**.

## Features

- FastAPI REST API
- OpenAI Responses API integration
- Developer/system-level instructions
- User prompt handling
- Pydantic request validation
- Environment-based configuration
- OpenAI API error handling
- **Streaming LLM responses**
- **Streaming response handling with FastAPI**
- Automatic Swagger/OpenAPI documentation
- ReDoc API documentation

## Tech Stack

- **Python 3.12+**
- **FastAPI**
- **Uvicorn**
- **OpenAI API**
- **Pydantic**
- **python-dotenv**
- **uv** for dependency and environment management

## Project Structure

```text
3030-project-ai-assistant-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── chat_router.py
│   ├── chat_service.py
│   └── chat_models.py
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
└── uv.lock