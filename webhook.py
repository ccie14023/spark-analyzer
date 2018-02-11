from flask import Flask, request
import json
from spark import *

ROOM_NAME = "Webhook Test"

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
	data = json.loads(request.data)
	print data['data']['id']
	print get_message(data['data']['id'], BOT_TOKEN)['text']
	return "OK"

if __name__ == '__main__':
	
	f = open("token","r")
	token = f.read()[:-1]
	f.close()

	room_id = get_room_id(ROOM_NAME, token)

	app.run(host="0.0.0.0")