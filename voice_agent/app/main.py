from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.auth import router as auth_router
from app.api.whisper import router as whisper_router
from app.api.tts import router as tts_router
from app.api.chatgpt import router as chatgpt_router
from app.api.voice_agent import router as voice_agent_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this later)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(auth_router, prefix="/auth")
app.include_router(whisper_router, prefix="/whisper")
app.include_router(tts_router, prefix="/tts")
app.include_router(chatgpt_router, prefix="/chatgpt")
app.include_router(voice_agent_router, prefix="/voice-agent")

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")