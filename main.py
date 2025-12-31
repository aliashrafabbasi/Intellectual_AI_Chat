from fastapi import FastAPI
from app.api.v1.chat import router as chat_router

app=FastAPI(title="Intellectual Ai")

app.include_router(chat_router,prefix="/api/v1")

