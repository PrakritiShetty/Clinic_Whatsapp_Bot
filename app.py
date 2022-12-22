from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods = ['POST'])
def reply():
    incoming_msg = request.form.get('Body').lower()
    # 4 types of user input - 
    # hello - trigger to start convo
    # yes/no for 'do you want to start reminder
    # date for 'type the date'
    # reminder for 'type the message'
    response = MessagingResponse()
    message = response.message()

if __name__ == 'main':
    app.run(debug=True)