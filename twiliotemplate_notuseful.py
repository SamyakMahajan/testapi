from twilio.rest import Client

account_sid = 'ACcac64a7fd3d8c588ae857886acb0e122'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='hihihihih',
  to='whatsapp:+919013363029'
)

print(message.sid)