import whisper
from pydub import AudioSegment
import io

class WhisperService:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_file):
        """
        Transcribes an audio file using Whisper.
        :param audio_file: Path to the audio file or bytes object.
        :return: Transcribed text.
        """
        if isinstance(audio_file, bytes):
            audio_file = io.BytesIO(audio_file)
            audio = AudioSegment.from_file(audio_file)
            audio.export("temp.wav", format="wav")
            audio_file = "temp.wav"

        result = self.model.transcribe(audio_file)
        return result["text"]