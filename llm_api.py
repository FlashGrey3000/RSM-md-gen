import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": """Hola chica!""",
        }
    ],
    model="deepseek-r1-distill-llama-70b",
)

def generate_message(con):

    return 0

print(chat_completion.choices[0].message.content)