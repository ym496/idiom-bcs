import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)
file = sys.argv[1]

prompt = """ 
This is a transcript from one of the episodes of the TV series, Better Call Saul. I need you to extract and list idioms spoken by the characters, focusing only on phrases that have idiomatic meanings. Avoid trivial phrases, single-word expressions, or common everyday language that doesn't carry deeper meaning. The idioms should be useful in understanding the language and be appropriate for educational purposes. Also, ensure no copyrighted material or unsafe content is included in your response.

Output the result in markdown format using the following structure:

```markdown
## Episode: [Episode Title]

### Idiom: *[Idiom 1]*
- **Definition**: [Brief explanation of the idiom]
- **Usage in show**: "[The sentence or part of the dialogue where the idiom appears]"

---

### Idiom: *[Idiom 2]*
- **Definition**: [Brief explanation of the idiom]
- **Usage in show**: "[The sentence or part of the dialogue where the idiom appears]"

---
```
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
