from flask import Flask, request
import json
from spark import *

BOT_TOKEN = "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OLzlhZjRmNDllLTNmYTQtNDA0Yy04ZWRjLTYxZWEzMDMyYmJjYw"
ROOM_NAME = "Webhook Test"

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
	data = json.loads(request.data)
	print data['data']['id']
	print get_message(data['data']['id'], BOT_TOKEN)['text']
	return "OK"

if __name__ == '__main__':
	
	room_id = get_room_id(ROOM_NAME, BOT_TOKEN)

	app.run(host="0.0.0.0")