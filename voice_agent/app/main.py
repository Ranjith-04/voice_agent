from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.whisper import router as whisper_router
from app.api.tts import router as tts_router
from app.api.chatgpt import router as chatgpt_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(whisper_router, prefix="/whisper")
app.include_router(tts_router, prefix="/tts")
app.include_router(chatgpt_router, prefix="/chatgpt")

@app.get("/")
async def root():
    return {"message": "Welcome to the Voice Agent API!"}