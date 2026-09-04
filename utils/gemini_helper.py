import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-lite")  ## sdk Software Developer Kit (SDK)


def generate_farming_advice(prompt):

    response = model.generate_content(prompt)

    return response.text
