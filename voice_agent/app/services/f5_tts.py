import subprocess

class F5TTSService:
    def __init__(self, cli_path="f5-tts_infer-cli"):
        self.cli_path = cli_path

    def generate_speech(self, text, output_file="output.wav"):
        """
        Generates speech from text using F5-TTS.
        :param text: Input text for TTS.
        :param output_file: Output audio file path.
        :return: Path to the generated audio file.
        """
        command = [
            self.cli_path,
            "--gen_text", text,
            "--output_file", output_file
        ]
        subprocess.run(command, check=True)
        return output_file