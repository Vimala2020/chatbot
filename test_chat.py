import requests

# URL of your local Flask chatbot
url = "http://127.0.0.1:5000/chat"

# Example message
payload = {"message": "Hello"}

# Send POST request
res = requests.post(url, json=payload)

# Print the bot's reply
print(res.json())
