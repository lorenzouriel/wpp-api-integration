from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

# Environment variables
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")


def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v21.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_id,
        "type": "text",
        "text": {"body": message_text},
    }
    response = requests.post(url, headers=headers, json=payload)
    print("Response:", response.json())


# Example usage
send_message(PHONE_NUMBER, "Olá, como vai?")
