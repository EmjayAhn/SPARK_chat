<<<<<<< HEAD
from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app)

@app.route('/')
def hello_world():
    return "Hello Gaemigo Project Home Page!!"

@app.route('/chat')
def chatting():
    return render_template('chat.html')


@socket_io.on("message")
def request(message):
    print("message : "+ message)
    to_client = dict()
    if message == 'new_connect':
        to_client['message'] = "새로운 유저가 입장하였습니다."
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
    send(to_client, broadcast=True)



if __name__ == '__main__':
    socket_io.run(app, debug=True, port=9999)
=======
from flask import *
from flask_socketio import SocketIO, send

app = Flask(__name__)
socket_io = SocketIO(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

@socket_io.on("message")
def request(message):
    print("message : " + message)
    to_client = dict()
    if message == 'new_connect':
        to_client['message'] = '유저가 입장하였습니다.'
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'
    send(to_client, broadcast=True)

if __name__ == '__main__':
    socket_io.run(app, debug=True)
>>>>>>> d15d4250b7da8af62a8f78bcd2b2bd8624643351
