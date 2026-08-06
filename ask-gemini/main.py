from google import genai
from config import API_KEY

client = genai.Client(api_key = API_KEY)

def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model = "gemini-3.6-flash",
            contents = prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"

def menu():
    while True:
        print("\n===== Ask Gemini =====")
        print("1. Summarize Text")
        print("2. Translate Text")
        print("3. Generate Python Code")
        print("4. Generate Email")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            text = input("\nEnter the text to summarize:\n")
            prompt = f"Summarize the following text in 5 bullet points:\n\n{text} and Do not use markdown"
            print("\nResponse:\n")
            print(ask_gemini(prompt))

        elif choice == "2":
            text = input("\nEnter text:\n")
            language = input("Translate to: ")
            prompt = f"Translate the following text into {language}:\n\n{text} and Do not use markdown"
            print("\nResponse:\n")
            print(ask_gemini(prompt))

        elif choice == "3":
            task = input("\nDescribe the program:\n")
            prompt = (
                f"Write Python code for the following task:\n{task}\n"
                "Include comments and explain the code and Do not use markdown"
            )
            print("\nResponse:\n")
            print(ask_gemini(prompt))

        elif choice == "4":
            purpose = input("\nPurpose of the email: ")
            tone = input("Tone (formal/friendly): ")
            prompt = (
                f"Write a {tone} email about: {purpose}. "
                "Include a subject line. and Do not use markdown"
            )
            print("\nResponse:\n")
            print(ask_gemini(prompt))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()