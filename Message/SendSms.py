import datetime
import os
from twilio.rest import Client

sid = os.environ['SID']
authToken = os.environ['AUTH']

client = Client(sid, authToken)

class Mes:
	def message(visitor, time, hash_id):
		client.messages.create(to='+201016878461',from_='+19724356236',body=('You have a ' + str(visitor) + ' visitor at '+ str(time) + ' https://website.com/' + str(hash_id)))
