# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load API key from .env file
# load_dotenv()

# api_key = os.getenv("GOOGLE_API_KEY")

# if not api_key:
#     raise ValueError("GOOGLE_API_KEY not found in .env file")

# # Configure Gemini
# genai.configure(api_key=api_key)

# # Create model
# model = genai.GenerativeModel("gemini-2.5-flash")

# # Ask Gemini a question
# response = model.generate_content("Hello! Introduce yourself in 3 lines.")

# print(response.text)

import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Generate response
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Hello! Introduce yourself in 3 lines."
)

print(response.text)