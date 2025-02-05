from celery import Celery
from app.services.f5_tts import F5TTSService

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def generate_speech_task(text, output_file):
    tts_service = F5TTSService()
    tts_service.generate_speech(text, output_file)