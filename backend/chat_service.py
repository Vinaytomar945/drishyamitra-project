import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_ai(message):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant for a photo management system called DrishyaMitra. Help users manage their photos."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content