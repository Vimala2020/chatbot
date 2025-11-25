import os
from colorama import Fore, Style, init
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Set the credentials
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path

# -----------------------------
# 1️⃣ Initialize colorama
# -----------------------------
init(autoreset=True)

# -----------------------------
# 2️⃣ Set credentials
# -----------------------------
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ""

# -----------------------------
# 3️⃣ Suppress gRPC warnings
# -----------------------------
os.environ['GRPC_VERBOSITY'] = 'ERROR'
os.environ['GRPC_TRACE'] = ''

# -----------------------------
# 4️⃣ Load a valid Gemini model
# -----------------------------
model = genai.GenerativeModel("models/gemini-2.5-flash")  # use a model from list_models.py

print(Fore.YELLOW + "Gemini Chatbot ready! Type 'exit' to quit.\n")

# -----------------------------
# 5️⃣ Initialize conversation history
# -----------------------------
history = []
MAX_HISTORY = 10  # keeps last 10 messages for context

# -----------------------------
# 6️⃣ Start chat loop
# -----------------------------
while True:
    user = input(Fore.GREEN + "You: ")

    if user.lower() == "exit":
        print(Fore.YELLOW + "Exiting chatbot. Goodbye!")
        break

    # Add user message to history
    history.append({"text": user})
    history = history[-MAX_HISTORY:]  # keep only last MAX_HISTORY messages

    # Generate bot reply
    try:
        response = model.generate_content(history)
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = "Oops! Something went wrong. Please try again."
        print(Fore.RED + f"Error: {e}")

    # Print bot reply
    print(Fore.BLUE + "Bot:", bot_reply)

    # Add bot reply to history
    history.append({"text": bot_reply})
    history = history[-MAX_HISTORY:]  # keep history consistent

    # Optional: save chat history to a file
    with open("chat_history.txt", "a") as f:
        f.write(f"You: {user}\n")
        f.write(f"Bot: {bot_reply}\n")

