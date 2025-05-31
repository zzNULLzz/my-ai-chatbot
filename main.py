import groq
import os
from dotenv import load_dotenv

# Load .env file containing your API key
load_dotenv()

# Initialize the Groq client with your API key stored in .env as GROQ_API_KEY
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initial system instruction for the assistant
messages = [
    {
        "role": "system",
        "content": (
            "You are an expert-level AI assistant built to help Azaliah Mwangi. "
            "Azaliah is a talented 18-year-old aspiring software engineer and cybersecurity specialist, "
            "currently building freelancing skills in AI automation and systems. "
            "Respond in a friendly but advanced tone, like ChatGPT+, and give answers that are helpful, clear, and detailed."
        )
    }
]

print("🤖 Welcome back, Azaliah! Type 'exit' to stop the chat.")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("👋 Bye for now, Azaliah. Keep building cool stuff!")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("AI:", reply)

        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("⚠️  There was an error:", e)

