import os
from groq import Groq
from dotenv import load_dotenv

# Load the secret key from the .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

def get_agent_response(prompt: str) -> str:
    """
    Sends the prompt to the real Llama 3 model via Groq and returns the text.
    """
    if not client:
        return "Error: GROQ_API_KEY not found. Check your .env file."

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Answer this prompt as briefly as possible. Do not use full sentences unless necessary. Just provide the direct answer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="openai/gpt-oss-120b", # Free, incredibly fast model
            temperature=0.0, # Keep it strictly factual
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"