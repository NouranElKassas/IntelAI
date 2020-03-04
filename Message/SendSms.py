import datetime
import os
from twilio.rest import Client

sid = 'AC704449781a470b6f0bf9a888fe5245d0'
authToken = 'c8f0575f7ac5642968c0da1bbbeaf446'

client = Client(sid, authToken)

class Mes:
	def message(visitor, time, hash_id):
		client.messages.create(to='+201016878461',from_='+19724356236',body=('You have a ' + str(visitor) + ' visitor at '+ str(time) + ' https://website.com/' + str(hash_id)))
