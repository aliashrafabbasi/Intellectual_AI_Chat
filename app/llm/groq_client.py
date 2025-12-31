from langchain_groq import ChatGroq
from app.core.config import GROQ_API_KEY
from app.llm.prompts import INTELLECTUAL_PROMPT

client = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=GROQ_API_KEY
)

def get_ai_response(messages: list) -> str:
    response = client.invoke(messages)
    return response.content

