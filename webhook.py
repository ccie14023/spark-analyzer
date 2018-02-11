from flask import Flask, request
import json
from spark import *

ROOM_NAME = "Webhook Test"

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
	data = json.loads(request.data)
	msg_txt = parse_data(data)
	put_txt(msg_txt)
	return "OK"

def parse_data(data):
	new_msg_id = data['data']['id']
	resp = get_message(data['data']['id'], token)
	new_msg_d = json.loads(resp.text)
	return new_msg_d['text']

def put_txt(data):

	f = open("messages","a")
	f.write(data.encode("ascii","ignore"))
	f.write('\n')
	f.close()

if __name__ == '__main__':
	
	f = open("token","r")
	token = f.read()[:-1]
	f.close()

	room_id = get_room_id(ROOM_NAME, token)

	app.run(host="0.0.0.0")