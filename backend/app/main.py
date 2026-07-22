from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  app.router import chat_route
from app.core.lifespan import lifespan

app = FastAPI(
    title="Internal Knowledge Chatbot",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_route.router, prefix="/v1")


@app.get('/health-check')
def health():
    return {
        "message":"health is good"
    }
@app.get("/")
def home():
    return {
        "message": "RAG Chatbot API"
    }

