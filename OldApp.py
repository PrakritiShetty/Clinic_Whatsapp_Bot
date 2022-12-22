from flask import Flask, request
import os
# from googlesearch import search
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client


app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def reply():
	msg = request.form.get('Body').lower()

	print("msg=>", msg)
	resp = MessagingResponse()
	reply = resp.message()

	account_sid=os.environ['ACfbaf09f396affd820a988129dd37ed6e']
	auth_token=os.environ['e312bb5204395045c0d3097028789e9f']
	client=Client(account_sid, auth_token)

	# Create reply
	if(msg=="hi" or msg=="Hi" or msg=="HI"):
		message = client.messages \
			.create(
         body='Thank you for submitting your order. To finalize your payment, please tap below to call or visit our website.',
         from_='whatsapp:+15005550006',
         to='whatsapp:+14155238886')
		
		reply.body(message.sid)
	
	return str(resp)

# # chatbot logic
# def bot():

# 	# user input
# 	user_msg = request.values.get('Body', '').lower()

# 	# creating object of MessagingResponse
# 	response = MessagingResponse()

# 	# User Query
# 	q = user_msg + "geeksforgeeks.org"

# 	# list to store urls
# 	result = []

# 	# searching and storing urls
# 	for i in search(q, tld='co.in', num=6, stop=6, pause=2):
# 		result.append(i)

# 	# displaying result
# 	msg = response.message(f"--- Result for '{user_msg}' are ---")

# 	msg = response.message(result[0])
# 	msg = response.message(result[1])
# 	msg = response.message(result[2])
# 	msg = response.message(result[3])
# 	msg = response.message(result[4])

# 	return str(response)


if __name__ == "__main__":
	app.run(debug=True)
