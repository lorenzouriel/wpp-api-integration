# Flask WhatsApp Webhook and Message Sender

This project demonstrates how to set up a Flask-based webhook to receive messages from WhatsApp Business and a standalone script to send messages using the WhatsApp Business API. 

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Environment Variables](#environment-variables)
  - [Running the Webhook](#running-the-webhook)
  - [Configure your Webhook on Meta Developers Site](#configure-your-webhook-on-meta-developers-site)
  - [Testing Message Sending](#testing-message-sending)
- [Endpoints](#endpoints)
- [Notes](#notes)

## Overview

- **`app.py`**: A Flask application that acts as a webhook to receive WhatsApp Business messages.
- **`send_message.py`**: A Python script to send WhatsApp messages via the WhatsApp Business API.


## Features

- **Receive Messages**: Use `app.py` to receive messages via WhatsApp Business.
- **Send Messages**: Use `send_message.py` to send WhatsApp messages programmatically.
- **Webhook Verification**: Validate the webhook using the verification token.

## Requirements

- Python 3.12+
- Flask
- dotenv
- requests
- ngrok (for webhook testing)

## Setup

### 1. Environment Variables

Create a `.env` file in the project root with the following content:

```env
VERIFY_TOKEN=*****
ACCESS_TOKEN=*****
PHONE_NUMBER_ID=*****
PHONE_NUMBER=*****
```

### 2. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt

pip install flask python-dotenv requests
```

### 3. Running the Webhook
Start the Flask application:
```bash
python app.py

# Or

docker build -t wpp-api-integration .

docker run -p 5000:5000 --env-file .env wpp-api-integration
```

Expose the application using ngrok:
```bash
ngrok http 5000
```

Copy the forwarding URL (e.g., `https://<ngrok-url>.ngrok-free.app`) and use it to configure the webhook in WhatsApp Business Manager.

### 4. Configure your Webhook on Meta Developers Site
To receive alerts when a message arrives or when the status of a message changes, you need to configure a Webhooks endpoint for your application. [Learn how to configure Webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started#configure-webhooks).

### 5. Testing Message Sending
Run the send_message.py script to send a message:
```bash
python send_message.py
```

The script sends a message to the specified recipient number using the WhatsApp Business API.


## Endpoints
`GET /`
- Description: Health check endpoint.
- Response: `"API is up"`

`GET /webhook`
- Description: Validates the webhook with the hub.verify_token and responds with the hub.challenge value.
- Response:
    - `200 OK` if verification succeeds.
    - `403 Forbidden` if verification fails.

`POST /webhook`
- Description: Receives incoming webhook events from WhatsApp Business.
- Response: `"EVENT_RECEIVED"`

--- 
## Notes
- Update the `ACCESS_TOKEN` and `PHONE_NUMBER_ID` with your actual credentials from WhatsApp Business Manager.
- Replace `VERIFY_TOKEN` in the `.env` file and WhatsApp Business settings to match.
- Ensure the `ngrok URL` is updated whenever a new session is started.
- The `send_message.py` script requires a valid recipient phone number.