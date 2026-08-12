from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

loader = TextLoader("notes.txt", encoding="utf-8")
documents = loader.load()

context = documents[0].page_content

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash"
)

prompt = ChatPromptTemplate.from_template("""
Answer the question using only the following context.

Context:
{context}

Question:
{question}

If the answer cannot be found in the context, say:
"I don't know based on the provided document."
""")

chain = prompt | model | StrOutputParser()

while True:
    question = input("\nEnter your question: ")

    if question == "Quit":
        print("\nExiting")
        print("*" * 30)
        break

    answer = chain.invoke({
        "context" : context,
        "question" : question
    })

    # Display answer
    print("\nAnswer:")
    print(answer)