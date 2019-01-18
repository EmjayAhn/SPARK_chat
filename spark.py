from flask import Flask
from flask import render_template, url_for, request, redirect
from flask_socketio import SocketIO, send, leave_room

app = Flask(__name__)
socket_io = SocketIO(app)
data = {"sessions": {}, "current_users": {}, "messages": {}}

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def form():
    global username, profilecon
    if request.method == 'GET':
        username = request.args.get('username')
        profilecon = request.args.get('profilecon')
        return render_template('chat.html', username=username, profilecon=profilecon)


@socket_io.on("message")
def msg_send(message):
    global username, profilecon, data
    path = request.full_path.split("?")[1]
    if message == 'new_connect':
        data["user_no"] = len(data["current_users"])
        mysession = path.split("&")[2].split("=")[1]
        data["sessions"][mysession] = {"name": username, "con": profilecon}
        data['current_users'][username] = {"name": username, "con": profilecon, "mysession": mysession}
        data['messages']['user'] = username
        data['messages']['message'] = ' {} 님이 입장하였습니다.'.format(username)
        data['messages']['profilecon'] = profilecon
        data['messages']['type'] = 'connect'
        # data['messages']["path"] = path
    else:
        mysession = path.split("&")[2].split("=")[1]
        myname = data['sessions'][mysession]["name"]
        mycon = data['sessions'][mysession]["con"]
        data['messages']['user'] = myname
        data['messages']['message'] = message
        data['messages']['profilecon'] = mycon
        data['messages']['type'] = 'normal'
    send(data, broadcast=True)


# @socket_io.on("leave")
# def on_leave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', room=room)


if __name__ == '__main__':
    app.run(debug=True)
    socket_io.run(app, debug=True)
