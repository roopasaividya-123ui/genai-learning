# We are importing the tools we need
# dotenv helps us read the API key from .env file safely
from dotenv import load_dotenv

# os helps us talk to the computer's system (like reading files)
import os

# Groq is the AI company whose API we are using
from groq import Groq

# This line reads your .env file and loads the API key
# Without this, Python cannot find your key
load_dotenv()

# This gets the API key from .env file
# os.getenv looks for GROQ_API_KEY inside your .env file
api_key = os.getenv("GROQ_API_KEY")

# This creates your connection to the AI
# Think of this like logging into the AI server
client = Groq(api_key=api_key)

# This is the cost of this AI model per 1 million tokens
# We will use this to calculate how much each message costs
COST_PER_MILLION_INPUT_TOKENS = 0.59   # dollars
COST_PER_MILLION_OUTPUT_TOKENS = 0.79  # dollars

# This line prints a welcome message when you run the program
print("=" * 50)
print("   TOKEN VISUALIZER - Session 01")
print("=" * 50)
print()

# This loop keeps the program running
# It will keep asking you for input until you type 'quit'
while True:

    # This asks you to type something
    # input() waits for you to type and press Enter
    user_message = input("You: ")

    # If you type 'quit', the program stops
    if user_message.lower() == "quit":
        print("Goodbye! Great work today.")
        break

    # If you type nothing and just press Enter, ask again
    if user_message.strip() == "":
        print("Please type something first.")
        continue

    # This sends your message to the AI
    # model is which AI brain we are using
    # messages is the conversation — your message goes here
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    # This gets the AI's reply text from the response
    ai_reply = response.choices[0].message.content

    # This gets how many tokens were used
    # prompt_tokens = tokens in YOUR message
    # completion_tokens = tokens in AI's REPLY
    input_tokens = response.usage.prompt_tokens
    output_tokens = response.usage.completion_tokens
    total_tokens = response.usage.total_tokens

    # This calculates the cost in dollars
    # We divide by 1,000,000 because price is per million tokens
    input_cost = (input_tokens / 1_000_000) * COST_PER_MILLION_INPUT_TOKENS
    output_cost = (output_tokens / 1_000_000) * COST_PER_MILLION_OUTPUT_TOKENS
    total_cost = input_cost + output_cost

    # Now we print everything nicely
    print()
    print("AI:", ai_reply)
    print()
    print("-" * 50)
    print("TOKEN BREAKDOWN:")
    print(f"  Your message tokens  : {input_tokens}")
    print(f"  AI reply tokens      : {output_tokens}")
    print(f"  Total tokens used    : {total_tokens}")
    print()
    print("COST BREAKDOWN:")
    print(f"  Your message cost    : ${input_cost:.6f}")
    print(f"  AI reply cost        : ${output_cost:.6f}")
    print(f"  Total cost           : ${total_cost:.6f}")
    print(f"  Rs. approx           : ₹{total_cost * 84:.4f}")
    print("-" * 50)
    print()