from fastapi import APIRouter,HTTPException

from app.services.chat_services import (
    chat_with_ai,
    list_chats,
    get_chat,
    remove_chat

)
router = APIRouter()

@router.post("/chat")
def chat(session_id:str,message:str):
    reply=chat_with_ai(session_id,message)
    return {
        "session_id":session_id,
        "reply":reply
    }


@router.get("/chats")
def get_all_chats():
    return list_chats()

@router.delete("/chat/{session_id}")
def delete_chat(session_id:str):
    deleted = remove_chat(session_id)
    if deleted == 0:
        raise HTTPException(status_code=404,detail="Chat Not Found!")
    return {"message":"Chat Deleted successfuly!"}