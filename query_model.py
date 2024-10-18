import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

prompt = """ 

This a transcript of one the episode of the show, Better Call Saul. I want you to list down all the idioms they've used in a JSON format.

Only include idioms that were spoken by the character. Ignore it, if it's a descriptive text.

Use this JSON schema:
{
  "episode_title": "string",
  "episode_number": "integer",
  "idioms": [
    {
      "text": "string",
      "definition": "string",
      "usage in show": "string",
    }
  ]
}

"""
model = genai.GenerativeModel("gemini-1.5-flash")
ep_file = genai.upload_file("./ep-trans/S1ep01.txt")
response = model.generate_content([prompt, ep_file])
print(response.usage_metadata)
print(response.text)
