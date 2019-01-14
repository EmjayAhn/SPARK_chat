from flask import Flask
from flask import render_template, url_for, request, redirect
from flask_socketio import SocketIO, send, leave_room

app = Flask(__name__)
socket_io = SocketIO(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global username, profilecon
    if request.method == 'POST':
        username = request.form['username']
        profilecon = request.form['profilecon']
        return render_template('chat.html', username=username, profilecon=profilecon)

@socket_io.on("message")
def msg_send(message):
    global username, profilecon
    users = dict()
    if message == 'new_connect':
        users['message'] = '[{}]님이 입장하였습니다.'.format(username)
        users['profilecon'] = profilecon
        users['type'] = 'connect'
    else:
        users['message'] = '[' + username + ']' + ' : ' + message
        users['profilecon'] = profilecon
        users['type'] = 'normal'
    send(users, broadcast=True)

# @socket_io.on("leave")
# def on_leave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', room=room)


if __name__ == '__main__':
    app.run(debug=True)
    socket_io.run(app, debug=True)
