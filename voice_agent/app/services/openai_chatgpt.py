from portkey_ai import Portkey

class ChatGPTService:
    def __init__(self, api_key, model="gpt-4o-mini", provider="openai"):
        
        self.client = Portkey(
            provider=provider,  # e.g., "openai", "anthropic", "bedrock", etc.
            Authorization=api_key  # Your provider API key
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
                messages=[{"role": "user", "content": prompt}],
                model=self.model
            )
            return response.choices[0].message.content
        except Exception as e:
            # Log the error and raise it for debugging
            print(f"Error generating response: {e}")
            raise