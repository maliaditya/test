
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC9f3176c894b3ba79073dba0146d8b6e3'
auth_token = '313cef0fa632d53a2f10afeccd5ee366'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+19388883481',
                     to='+919765402942'
                 )

print(message.sid)