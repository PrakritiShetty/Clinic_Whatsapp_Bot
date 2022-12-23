from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gsheet_func import *
from dateutil.parser import parse

app = Flask(__name__)
count=0

@app.route("/sms", methods = ['POST'])
def reply():

    incoming_msg = request.form.get('Body').lower()
    # 4 types of user input - 
    # hello - trigger to start convo
    # yes/no for 'do you want to start reminder
    # date @'type the date'
    # reminder @'type the message'
    response = MessagingResponse()
    print(incoming_msg)
    message = response.message()
    responded = False
    words = incoming_msg.split('@')


    # chatbot functions
    # set_reminder_date
    # set_reminder_body
    # save to gsheets using gspread package

    if "hello" in incoming_msg:
        reply = "Hello! \n Do you want to set a reminder?"
        message.body(reply)
        responded=True
    

if __name__ == 'main':
    app.run(debug=True)