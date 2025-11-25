import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
from flask_cors import CORS   # <-- ADD THIS

# Load .env file
load_dotenv()

# Set the credentials
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path

app = Flask(__name__)

# ENABLE CORS (IMPORTANT FOR FRONTEND)
CORS(app)

os.environ['GRPC_VERBOSITY'] = 'ERROR'
os.environ['GRPC_TRACE'] = ''

# Load model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# In-memory chat history
conversation_history = []

@app.route("/", methods=["GET"])
def home():
    return "Backend is running!"

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    data = request.get_json()
    user_message = data.get("message", "")
    
    # Add user message
    conversation_history.append({"text": user_message})
    conversation_history = conversation_history[-10:]

    try:
        response = model.generate_content(conversation_history)
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    # Add bot reply
    conversation_history.append({"text": bot_reply})
    conversation_history = conversation_history[-10:]

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
