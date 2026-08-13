import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

chat = client.chats.create(
    model="gemini-3.6-flash",
    config={
        "system_instruction": (
            "You are a helpful AI assistant. "
            "Give clear and concise answers. "
            "Do not give answers in Markdown"
            "If you don't know something, say so."
        )
    }
)

print("=" * 40)
print("       Simple AI Chatbot")
print("=" * 40)
print("Type /exit to quit")
print("Type /clear to clear the conversation")
print()

while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "/exit":
        print("Goodbye")
        break

    if user_input.lower() == "/clear":
        chat = client.chats.create(
            model="gemini-3.6-flash",
            config={
                "system_instruction": (
                    "You are a helpful AI assistant. "
                    "Give clear and concise answers. "
                    "If you don't know something, say so."
                )
            }
        )

        print("Conversation cleared.\n")
        continue

    try:
        print("AI is thinking...")
        response = chat.send_message(user_input)    
        print("AI:", response.text)

    except Exception as e:
        print("Error:", e)