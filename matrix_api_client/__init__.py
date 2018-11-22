import requests

class Matrix(object):
	"""docstring for Matrix"""
	def __init__(self, access_token, server, room_id, debug=0):
		
		self.access_token = access_token
		self.server = server
		self.room_id = room_id	# for now we care about a single room

		# define the request url as a variable for convenience. If we eventually care about >1 rooms, will need to modify
		self.request_url = '{}{}/send/m.room.message?access_token={}'.format(self.server,self.room_id,self.access_token)

		# define the fetch url as well, TODO: abstract this somehow?
		self.fetch_url = '{}{}/messages?access_token={}'.format(self.server,self.room_id,self.access_token)


	def send_message(self,message):
		'''sends a message'''
		# todo: add a message_type to the arguments which allows the user to specify e.g., text, image

		body = {
			'msgtype' : 'm.text',	# hardcoded for now? 
			'body' : message
		}

		if self.debug == 1:
			print('sending message to {}'.format(self.request_url))
			print('message body: {}'.format(message))
		r = requests.post(self.request_url,json=body)

		return(r.text)

	def get_messages(self):
		''' gets a start - stop timestamp of messages?'''
		# TODO: more on getting events is here: https://matrix.org/docs/guides/client-server.html
		
		if self.debug == 1:
			print('fetching results from {}'.format(self.fetch_url))
		r = requests.get(self.fetch_url)
		return(r.json())

