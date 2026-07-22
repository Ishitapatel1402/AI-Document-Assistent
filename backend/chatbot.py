from google import genai

from backend.config import GOOGLE_API_KEY
from backend.config import MODEL_NAME

client = genai.Client(api_key=GOOGLE_API_KEY)


def get_response(prompt):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text