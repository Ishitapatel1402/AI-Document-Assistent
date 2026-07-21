from google import genai

from backend.config import GOOGLE_API_KEY, MODEL_NAME
from backend.prompts import SYSTEM_PROMPT

client = genai.Client(api_key=GOOGLE_API_KEY)


def get_response(user_input):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"{SYSTEM_PROMPT}\n\nUser Question:\n{user_input}"
    )

    return response.text