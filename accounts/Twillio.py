# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['ACba5f005498930aa19505d7407260b5d3']
# auth_token = os.environ['8c2eadb272e87d25678ca16a1713f6d1']
def twilio(otp):
	client = Client('ACba5f005498930aa19505d7407260b5d3', '8c2eadb272e87d25678ca16a1713f6d1')
	# tel = "+91"
	body = "Your OTP is {}".format(otp)
	message = client.messages \
	.create(
		body=body,
		from_='+12156083914',
		to= '+918219773675'
		)
	print(message.sid)

