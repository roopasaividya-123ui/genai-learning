from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: API key not found. Check your .env file.")
else:
    print("API key loaded!")
    print("Key preview:", api_key[:12] + "...")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Say hello in one sentence."}
    ]
)

print("")
print("AI says:", response.choices[0].message.content)
print("")
print("Input tokens:", response.usage.prompt_tokens)
print("Output tokens:", response.usage.completion_tokens)
print("Total tokens:", response.usage.total_tokens)
print("")
print("Setup complete! Ready to build.")