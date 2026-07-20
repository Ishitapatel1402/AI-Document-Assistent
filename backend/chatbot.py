import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key and model name
api_key = os.getenv("GOOGLE_API_KEY")
model_name = os.getenv("MODEL_NAME")

# Create Gemini client
client = genai.Client(api_key=api_key)


def get_response(user_input):
    """
    Sends the user's message to Gemini
    and returns the generated response.
    """

    response = client.models.generate_content(
        model=model_name,
        contents=user_input
    )

    return response.text