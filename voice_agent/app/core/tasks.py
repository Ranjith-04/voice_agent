from celery import Celery

from app.core.config import settings

# Initialize the Celery app
celery_app = Celery(
    "tasks",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

# Optional: Configure Celery settings
celery_app.conf.update(
    result_expires=3600,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

# Define a Celery task
@celery_app.task
def generate_speech_task(text: str, output_file: str):
    """
    A Celery task to generate speech using F5-TTS.
    """
    from app.services.f5_tts import F5TTSService  # Import here to avoid circular imports
    tts_service = F5TTSService(cli_path=settings.F5_TTS_CLI_PATH)
    tts_service.generate_speech(text, output_file)