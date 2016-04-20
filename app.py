from flask import Flask, render_template
from twilio.rest import TwilioRestClient
import unicodecsv

app = Flask(__name__)

@app.route("/landingPage")
def landingPage():
    return render_template("index.html")

@app.route("/send", methods=['POST'])
def send():
    print "sent text"
# Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC651dcd0b578ee9f523abfb0de332b948"
    auth_token  = "c65b08717f3dd6727a4c845809088cb8"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body="Jenny please?! I love you <3",
        to="+447853263417",    # Replace with your phone number
        from_="+441278393077") # Replace with your Twilio number
    print message.sid

    smss = client.sms.messages.list()
    print smss

   # def smslist(sms_messages):
    #    with open(sms_messages) as csvfile:
     #       reader = unicodecsv.DictReader(sms_messages)

      #      for row in reader:
       #         print row Direction
        #        print row DateSent
         #       print row To
          #      print row From
           #     print row Body

    # smslist('sms_messages.csv')


    #https://api.twilio.com/2010-04-01/Accounts/AC651dcd0b578ee9f523abfb0de332b948/SMS/Messages.csv?PageSize=1000
    # export the raw data of messages from twilio






if __name__ == "__main__":
    app.run()
