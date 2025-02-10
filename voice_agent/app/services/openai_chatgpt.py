from openai import OpenAI

class ChatGPTService:
    def __init__(self, api_key, model="gpt-4o", provider="openai"):
        """
        Initialize the ChatGPTService with the OpenAI client configured for Portkey's gateway.
        :param api_key: Your OpenAI API key (or provider-specific API key).
        :param portkey_api_key: Your Portkey API key.
        :param model: The model to use for generating responses (default: gpt-4o-mini).
        :param provider: The LLM provider (default: openai).
        """
        self.client = OpenAI(
            api_key="EGOTgW4NfP9ddGndBpoAbCmGhAxR",  # Provider-specific API key (e.g., OpenAI API key)
            base_url="https://api.portkey.ai/v1",  # Point to Portkey's gateway URL
            default_headers={
                "x-portkey-api-key": "EGOTgW4NfP9ddGndBpoAbCmGhAxR",  # Portkey API key
                "x-portkey-provider": provider,       # Provider (e.g., "openai")
                "x-portkey-virtual-key": "open-ai-be92f5",
                "Content-Type": "application/json"
            }
        )
        self.model = model

    def generate_response(self, prompt):
        """
        Generate a response from the ChatGPT model.
        :param prompt: The input text for the model.
        :return: Generated response text.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            # Log the error and raise it for debugging
            print(f"Error generating response: {e}")
            raise