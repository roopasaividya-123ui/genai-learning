# Import tools we need
from dotenv import load_dotenv
import os
from groq import Groq

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Connect to Groq AI
client = Groq(api_key=api_key)

# This function sends any message to AI and returns reply
# We made it a function so we can reuse it 3 times
# prompt = the message we send to AI
def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        # max_tokens limits how long the answer can be
        # We use 200 so answers are short and easy to compare
        max_tokens=200
    )
    # Return just the text reply and token count
    return response.choices[0].message.content, response.usage.total_tokens

# Print welcome message
print("=" * 60)
print("   PROMPT COMPARISON TOOL - Session 02")
print("=" * 60)
print()
print("This tool shows how asking differently changes the answer.")
print()

# Keep running until user types quit
while True:

    # Ask user for their topic/question
    topic = input("Enter your topic (or 'quit' to exit): ")

    if topic.lower() == "quit":
        print("Goodbye! Great work today.")
        break

    if topic.strip() == "":
        print("Please type something.")
        continue

    print()
    print("Sending to AI in 3 different ways... please wait")
    print()

    # ─────────────────────────────────────────
    # PROMPT STYLE 1 — ZERO SHOT
    # Zero shot means: just ask directly, no examples
    # no role, no context — plain simple question
    # ─────────────────────────────────────────
    prompt1 = topic

    # ─────────────────────────────────────────
    # PROMPT STYLE 2 — DETAILED PROMPT
    # We add instructions to make answer better
    # Tell AI exactly what format we want
    # ─────────────────────────────────────────
    prompt2 = f"""Explain {topic} clearly with:
- A simple one line definition
- One real world example
- Why it matters
Keep it short and easy to understand."""

    # ─────────────────────────────────────────
    # PROMPT STYLE 3 — ROLE PROMPTING
    # We give AI a role/personality
    # This changes how it thinks and responds
    # ─────────────────────────────────────────
    prompt3 = f"""You are an experienced teacher explaining 
to a student who is hearing about {topic} for the very 
first time. Use simple words, a fun analogy, and make 
it memorable. Maximum 5 sentences."""

    # Send all 3 prompts to AI
    reply1, tokens1 = ask_ai(prompt1)
    reply2, tokens2 = ask_ai(prompt2)
    reply3, tokens3 = ask_ai(prompt3)

    # Print results side by side for easy comparison
    print("=" * 60)
    print("STYLE 1 — ZERO SHOT (just ask directly)")
    print("=" * 60)
    print(f"Prompt sent: '{prompt1}'")
    print()
    print("Answer:", reply1)
    print(f"Tokens used: {tokens1}")

    print()
    print("=" * 60)
    print("STYLE 2 — DETAILED PROMPT (with instructions)")
    print("=" * 60)
    print(f"Prompt sent: '{prompt2}'")
    print()
    print("Answer:", reply2)
    print(f"Tokens used: {tokens2}")

    print()
    print("=" * 60)
    print("STYLE 3 — ROLE PROMPTING (give AI a role)")
    print("=" * 60)
    print(f"Prompt sent: '{prompt3}'")
    print()
    print("Answer:", reply3)
    print(f"Tokens used: {tokens3}")

    print()
    print("─" * 60)
    print("COMPARISON SUMMARY:")
    print(f"  Zero shot tokens    : {tokens1}")
    print(f"  Detailed tokens     : {tokens2}")
    print(f"  Role prompt tokens  : {tokens3}")
    print(f"  Total tokens used   : {tokens1 + tokens2 + tokens3}")
    print("─" * 60)
    print()
    print("NOTICE:")
    print("  - Did Style 2 give a more structured answer?")
    print("  - Did Style 3 use simpler words?")
    print("  - Which style gave the best answer for your topic?")
    print()