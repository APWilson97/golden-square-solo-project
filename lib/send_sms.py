import os
from twilio.rest import Client 
from datetime import datetime, timedelta

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

time_now = datetime.now()
delivery_time = time_now + timedelta(minutes = 30)

time_now_string = time_now.strftime("%H:%M")
delivery_time_string = delivery_time.strftime("%H:%M")

message = client.messages.create(
    body=f"Thank you! Your order was placed and it will be delivered before {delivery_time_string}",
    from_='+447401119572',
    to='+447787447122'
)

print(message.sid)
