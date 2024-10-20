import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)
file = sys.argv[1]

prompt = """ 

This a transcript of one the episode of the show, Better Call Saul. I want you to list down all the idioms they've used in a markdown format. Please only include idioms that were spoken by the character. Focus on phrases that are commonly used and have metaphorical meanings. Avoid trivial or single-word expressions. Be careful to not include any unsafe or too sexual content. 

Use this markdown schema:
## Episode: [Episode Title]

### Idiom: *[Idiom 1]*
- **Definition**: [Brief explanation of the idiom]
- **usage in show**: "[The sentence where the idiom appears]"
---

### Idiom: *[Idiom 2]*
- **Definition**: [Brief explanation of the idiom]
- **usage in show**: "[The sentence where the idiom appears]"
---

*... and so on for each idiom found...*
"""
model = genai.GenerativeModel("gemini-1.5-flash")
ep_file = genai.upload_file(file)
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]
response = model.generate_content([prompt, ep_file],safety_settings=safety_settings)
print(response.text)
