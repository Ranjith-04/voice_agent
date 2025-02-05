from fastapi import APIRouter, File, UploadFile
from app.services.whisper import WhisperService

router = APIRouter()
whisper_service = WhisperService()

@router.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    content = await file.read()
    transcription = whisper_service.transcribe(content)
    return {"transcription": transcription}