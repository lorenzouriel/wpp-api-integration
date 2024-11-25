from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Environment variables
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

@app.route('/', methods=['GET'])
def home():
    return "API is up", 200

# Verification endpoint
@app.route("/webhook", methods=["GET"])
def verify_webhook():
    verify_token = "mytoken"
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == verify_token:
        return challenge, 200
    return "Forbidden", 403


# Webhook endpoint to receive messages
@app.route("/webhook", methods=["POST"])
def handle_webhook():
    data = request.get_json()

    if data:
        # Log the received data
        print("Received data:", data)

        # Handle the incoming messages
        if "messages" in data.get("entry", [{}])[0].get("changes", [{}])[0].get(
            "value", {}
        ):
            messages = data["entry"][0]["changes"][0]["value"]["messages"]
            for message in messages:
                handle_message(message)

    return "EVENT_RECEIVED", 200


def handle_message(message):
    sender_id = message["from"]  # Sender's WhatsApp ID
    text = message.get("text", {}).get("body", "")  # Message text
    print(f"Message from {sender_id}: {text}")

    # You can add logic to send replies using the WhatsApp Business API here.


if __name__ == "__main__":
    app.run(port=5000)
