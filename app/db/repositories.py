from datetime import datetime
from app.db.mongo import chats_collection


def get_chat(session_id:str):
    return chats_collection.find_one({"session_id":session_id})

def create_chat(session_id:str):
    chat={
        "session_id":session_id,
        "messages":[],
        "created_at":datetime.utcnow()
    }
    chats_collection.insert_one(chat)
    return chat

def add_messages(session_id:str , role:str,content:str):
    chats_collection.update_one(
        {"session_id":session_id},
        {"$push":{"message":{"role":role ,"content":content}}}
    )


def get_all_chats():
    return list(chats_collection.find({},{"_id":0}))

def delete_chat_by_session(session_id: str):
    result = chats_collection.delete_one({"session_id": session_id})
    return {"deleted_count": result.deleted_count}


from app.db.mongo import chats_collection

def add_message(session_id: str, role: str, content: str):
    chats_collection.update_one(
        {"session_id": session_id},
        {
            "$push": {
                "messages": {
                    "role": role,
                    "content": content
                }
            }
        }
    )
