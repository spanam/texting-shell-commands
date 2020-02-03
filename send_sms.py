# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC133f253158b30b4faf4f570c5adda845'
auth_token = 'cfaa6ea944bfae6567a43ae68c862a7f'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Test Message! See if it works",
                     from_='+12565107487',
                     to='+19147722087'
                 )

print(message.sid)
