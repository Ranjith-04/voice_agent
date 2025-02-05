from pydantic_settings import BaseSettings  # Import from pydantic_settings

class Settings(BaseSettings):
    # FastAPI settings
    APP_NAME: str = "Voice Agent API"
    DEBUG: bool = True

    # Database settings
    DATABASE_URL: str = "sqlite:///./test.db"  # Replace with your database URL
    DB_ECHO: bool = False

    # Authentication settings
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Celery settings
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"

    # OpenAI and F5-TTS settings
    PORTKEY_API_KEY: str = "EGOTgW4NfP9ddGndBpoAbCmGhAxR"
    F5_TTS_CLI_PATH: str = "f5-tts_infer-cli"

    class Config:
        env_file = ".env"  # Load environment variables from a .env file


settings = Settings()