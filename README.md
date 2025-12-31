# Intellectual AI Chat 🤖

A production-ready AI chat backend built with **FastAPI**, **MongoDB**, and **Groq LLM**.
Supports chat memory, summarization, and scalable API design.

---

## 🚀 Features
- FastAPI REST APIs
- Chat memory (MongoDB)
- LLM integration (Groq)
- Clean layered architecture
- Ready for production deployment

---

## 🧠 Tech Stack
- Python 3.12
- FastAPI
- MongoDB
- LangChain + Groq
- Uvicorn

---

## 📂 Project Structure
app/
├── api/v1 # Routes
├── services # Business logic
├── db # Mongo connection & queries
├── llm # AI clients & prompts
├── models # Pydantic models
└── core # Config & constants
---

## ⚙️ Setup

```bash
git clone git@github.com:aliashrafabbasi/Intellectual_AI_Chat.git
cd Intellectual_AI_Chat
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
Create .env:

MONGO_URI=your_mongo_uri
GROQ_API_KEY=your_groq_key


Run server:

uvicorn main:app --reload

📡 API Docs

Visit:
👉 http://127.0.0.1:8000/docs

🧪 Example Endpoint
POST /api/v1/chat?session_id=abc123&message=Hello

📌 Status

✅ Chat memory
✅ Summarization
🔜 Auth & rate limiting

🧑‍💻 Author

Ali Ashraf Abbasi


👉 Is README ko paste karo, commit & push later.

---

# ✅ 2️⃣ MongoDB Indexes (VERY IMPORTANT 🔥)

### ❌ Problem (without indexes)
- Chat history slow
- Memory retrieval expensive
- Scale pe lag

### ✅ Solution: indexes

Open Mongo shell / Compass and run:

```js
db.chats.createIndex({ session_id: 1 })
db.chats.createIndex({ created_at: -1 })


Agar messages embedded hain:

db.chats.createIndex({ "messages.timestamp": -1 })

🎯 Benefit

Fast chat recall

Summarization smooth

Production-safe

✅ 3️⃣ Production Tips (Real-world)
🔐 Environment

.env NEVER commit (already correct ✅)

Use dotenv only locally

Production me env vars system se

🚦 Rate Limiting (next logical step)

Add later:

slowapi or

API Gateway (NGINX / Cloudflare)

⚡ Uvicorn (Production)

Never use --reload in prod:

uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

🧠 Memory Control

You already solved:

context window limit

summarization

Next upgrade:

per-user memory limit

TTL index (auto delete old chats)

db.chats.createIndex({ created_at: 1 }, { expireAfterSeconds: 2592000 })


(30 days auto cleanup)

🏁 Verdict

This project is now:

❌ NOT tutorial-level

✅ REAL backend engineer level

✅ Resume + portfolio worthy

✅ Extendable to SaaS
