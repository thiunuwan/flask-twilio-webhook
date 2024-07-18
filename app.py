import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
app = Flask(__name__)
load_dotenv()
client = Client()

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route('/api/message', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()
    if message:
        return respond(f'Thank you for your message: "{message}". A member of our team will be in touch with you soon.')

@app.route('/api/hello', methods=['GET'])
def hello():
    return 'Hello there..!'

if __name__ == "__main__":
    app.run()
    