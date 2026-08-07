from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)

history = []
try:
    while True:
        prompt = input("\nEnter your prompt: ")

        if prompt.lower() == "exit":
            print("\nThank you for using our termminal chatbot")
            break


        history.append(f"User: {prompt}")

        response = client.models.generate_content(
            model = "gemini-3.6-flash",
            contents = "\n".join(history)
        )

        print("Gemini:", response.text)
except Exception as e:
    print("\nError :", e)
