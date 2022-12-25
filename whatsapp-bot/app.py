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
    if len(words)==1 and "yes" in incoming_msg:
        reminder_string = "Please provide a date in the following format \n\n Date@<type the date>"
        message.body(reminder_string)
        responded=True
    if len(words)==1 and "no" in incoming_msg:
        reply="Okay! Have a nice day"
        message.body(reply)
        responded=True
    elif len(words) !=1:
        input_type = words[0].strip().lower()
        input_string = words[1].strip()

        if input_type == "date":
            reply = "Please enter the reminder message in the following format only \n\n Reminder@<type the message>"
            set_reminder_date(input_string)
            message.body(reply)
            responded= True
        if input_type == "reminder":
            reply = "Your reminder is set!"
            set_reminder_body(input_string)
            message.body(reply)
            responded= True
        if not responded:
            message.body("Incorrect request format, please enter in the correct format")

        return str(response)
    

def set_reminder_date(msg):
    p=parse(msg)
    date=p.strftime('%d/%m/%Y')
    save_reminder_date(date)
    return 0


def set_reminder_body(msg):
    save_reminder_body(msg)
    return 0

if __name__ == 'main':
    app.run(debug=True)