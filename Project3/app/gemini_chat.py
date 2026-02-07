# import os
# from dotenv import load_dotenv
# from google import genai

# # 🔥 VERY IMPORTANT
# load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

# API_KEY = os.getenv("GEMINI_API_KEY")

# if not API_KEY:
#     raise ValueError("GEMINI_API_KEY not found. Check .env file location.")

# client = genai.Client(api_key=API_KEY)


# def chat_with_memory(user_input):
#     response = client.models.generate_content(
#         model="models/gemini-1.0-pro",
#         contents=user_input
#     )
#     return response.text

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def chat_with_memory(user_input):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_input
    )
    return response.text

