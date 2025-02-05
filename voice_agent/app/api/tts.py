from fastapi import APIRouter, Body
from app.services.f5_tts import F5TTSService

router = APIRouter()
tts_service = F5TTSService()

@router.post("/synthesize/")
async def synthesize_speech(text: str = Body(..., embed=True)):
    audio_file = tts_service.generate_speech(text)
    return {"audio_file": audio_file}