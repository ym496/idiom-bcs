import pathlib
import textwrap

import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)


query = "what's the purpose of life? how to find a purpose?"
prompt = query
model = genai.GenerativeModel('gemini-1.5-pro-latest')
response = model.generate_content(prompt)
print(response.text)
