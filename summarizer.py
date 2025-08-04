import os
from openai import OpenAI
from dotenv import load_dotenv

# ✅ Load .env
load_dotenv()

# ✅ Get API Key
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Initialize client
client = OpenAI(api_key=api_key)

def summarize_text(content):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes long content for PowerPoint slides."},
            {"role": "user", "content": f"Summarize this into slide points:\n\n{content}"}
        ]
    )
    return response.choices[0].message.content.strip()
