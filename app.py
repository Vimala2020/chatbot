import os
from flask import Flask, request, jsonify
import google.generativeai as genai

# -----------------------------
# 1️⃣ Flask app setup
# -----------------------------
app = Flask(__name__)

# -----------------------------
# 2️⃣ Credentials
# -----------------------------
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ""
os.environ['GRPC_VERBOSITY'] = 'ERROR'
os.environ['GRPC_TRACE'] = ''

# -----------------------------
# 3️⃣ Load model
# -----------------------------
model = genai.GenerativeModel("models/gemini-2.5-flash")

# -----------------------------
# 4️⃣ In-memory conversation storage
# -----------------------------
conversation_history = []

# -----------------------------
# 5️⃣ Flask route for chatbot
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    data = request.get_json()
    user_message = data.get("message", "")
    
    # Add user message to history
    conversation_history.append({"text": user_message})
    conversation_history = conversation_history[-10:]  # last 10 messages

    try:
        response = model.generate_content(conversation_history)
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = "Error: something went wrong."
    
    # Add bot reply to history
    conversation_history.append({"text": bot_reply})
    conversation_history = conversation_history[-10:]

    return jsonify({"reply": bot_reply})

# -----------------------------
# 6️⃣ Run server
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

