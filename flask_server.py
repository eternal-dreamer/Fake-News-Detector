from flask import Flask, request,jsonify
from os import environ
from twilio.twiml.messaging_response import MessagingResponse
from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL
from ml_model import *
import csv
app = Flask(__name__)
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    #this is data retrival
    msg = request.form.get('Body')
    # row=[]
    # row.append(message)
    resp = MessagingResponse()
    final_ans=income_message(str(msg))
    if(final_ans==1):
        resp.message("Real news you can share ")
        # row.append(1)
    else :
        resp.message("Fake news kindly report")
        # row.append(0)    

    # Create reply
    # with open("new_database.csv","w") as file:
        # csvwriter= csv.writer(file)
        # csvwriter.writerow(row)
    #this is data sending
    
    # resp.message("You said: {}".format(msg))

    return str(resp)


@app.route('/telegram', methods=['POST'])
def index():
    req = request.get_json()
    bot = TelegramBot()
    bot.parse_webhook_data(req)
    # success = bot.action()
    message = bot.return_message()
    final_ans = income_message(str(message))
    if(final_ans==1):
        success=bot.send_message("Real new , You can safely forward")
    else:
        success=bot.send_message("Fake new , kindly report")

    return jsonify(success=success) # TODO: Success should reflect the success of the reply

if __name__ == "__main__":
	app.run()
