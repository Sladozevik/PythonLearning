import twilio
print(twilio.__version__)

from twilio.rest import TwilioRestClient

account_sid = "{{ ACa658eb7e1629eb3ed50c57e4e89482b5 }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ 6e388672b035705371f67333b93be212 }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python, man",
    to="+385914621804",    # Replace with your phone number
    from_="+12015711016") # Replace with your Twilio number

print(message.sid)

print('pokusavamo sljedeci...')

# from twilio import TwilioRestException
# from twilio.rest import TwilioRestClient

# account_sid = "{{ ACa658eb7e1629eb3ed50c57e4e89482b5 }}" # Your Account SID from www.twilio.com/console
# auth_token  = "{{ 6e388672b035705371f67333b93be212 }}"  # Your Auth Token from www.twilio.com/console

# client = TwilioRestClient(account_sid, auth_token)

# try:
#     message = client.messages.create(body="Hello from Python",
#         to="+385914621804",    # Replace with your phone number
#         from_="+12015711016") # Replace with your Twilio number
# except TwilioRestException as e:
#     print(e)