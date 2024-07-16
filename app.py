import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

load_dotenv()

app = Flask(__name__)
client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route('/message', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()
    if message:
        return respond(f'Thank you for your message! A member of our team will be in touch with you soon.')

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello! Welcome !'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
