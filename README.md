# Flask Twilio Webhook

This project demonstrates the integration of a Flask application with Twilio to handle incoming messages via a webhook.

## Description

This Flask application receives incoming SMS messages using a Twilio webhook, processes the message content, and responds with a confirmation message including the received text.

When a message is sent to your Twilio number, Twilio will send a POST request to the `/api/message` endpoint of this application. The application then extracts the message content, processes it, and sends back a response acknowledging the received message.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/thiunuwan/flask-twilio-webhook.git
    cd flask-twilio-webhook
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the Flask application:

    ```bash
    python app.py
    ```

4. Set up a ngrok tunnel (optional for local development):

    ```bash
    ngrok http 5000
    ```

5. Configure your Twilio number's webhook URL to point to your server's URL followed by `/api/message`.

