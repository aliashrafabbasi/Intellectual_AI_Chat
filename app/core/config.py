from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

GROQ_API_KEY =os.getenv("GROQ_API_KEY")

CHAT_MEMORY_DAYS = 7