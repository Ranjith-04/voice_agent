from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from typing import Optional
import os
import uuid
from app.services.whisper import WhisperService
from app.services.openai_chatgpt import ChatGPTService
from app.services.f5_tts import F5TTSService
from app.utils.audio_utils import get_recorded_audio_data

router = APIRouter()

# Initialize services
whisper_service = WhisperService()
chatgpt_service = ChatGPTService(api_key="your-openai-api-key")
tts_service = F5TTSService(cli_path="f5-tts_infer-cli")

@router.post("/voice-pipe/")
async def voice_agent(audio_file: Optional[UploadFile] = File(None)):
    try:
        # Handle uploaded audio file
        if audio_file:
            file_content = await audio_file.read()
            file_extension = os.path.splitext(audio_file.filename)[-1]
        else:
            # Handle recorded audio (binary data)
            recorded_audio_data = await get_recorded_audio_data()
            file_content = recorded_audio_data
            file_extension = ".wav"

        # Generate a unique filename
        temp_file_name = f"temp_input_audio_{uuid.uuid4()}{file_extension}"
        with open(temp_file_name, "wb") as f:
            f.write(file_content)

        # Transcribe audio to text (STT)
        transcribed_text = whisper_service.transcribe(temp_file_name)
        print(f"Transcribed Text: {transcribed_text}")
        
        # Generate a response using ChatGPT (LLM)
        response_text = chatgpt_service.generate_response(transcribed_text)
        print(f"ChatGPT Response: {response_text}")

        # Convert the response text to speech (TTS)
        output_file = f"output_speech_{uuid.uuid4()}.wav"
        tts_service.generate_speech(response_text, output_file=output_file)

        # Return a JSON response
        return JSONResponse(content={"file_path": output_file}, media_type="application/json")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, media_type="application/json", status_code=500)
