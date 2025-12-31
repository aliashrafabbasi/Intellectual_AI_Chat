from app.db.repositories import get_chat, create_chat, add_message,get_all_chats
from app.llm.groq_client import get_ai_response
from app.llm.prompts import INTELLECTUAL_PROMPT

def chat_with_ai(session_id: str, user_message: str):
    chat = get_chat(session_id)

    if not chat:
        chat = create_chat(session_id)

    messages = [
        {"role": "system", "content": INTELLECTUAL_PROMPT}
    ]

    for msg in chat["messages"]:
        messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    messages.append({"role": "user", "content": user_message})

    ai_response = get_ai_response(messages)

    add_message(session_id, "user", user_message)
    add_message(session_id, "assistant", ai_response)

    return ai_response

def list_chats():
    return get_all_chats()

from app.db.repositories import delete_chat_by_session

def remove_chat(session_id: str):
    return delete_chat_by_session(session_id)


