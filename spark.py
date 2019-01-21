from flask import Flask
from flask import render_template, url_for, request, redirect
from flask_socketio import SocketIO, send, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socket_io = SocketIO(app)
data = {"sessions": {}, "current_users": {}, "chat": {}}

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
def msg_send(message, charset="UTF-8"):
    global username, profilecon, data
    path = request.full_path.split("?")[1]
    if message == 'new_connect':
        sessionid = request.sid
        data["user_no"] = len(data["current_users"])
        data["sessions"][sessionid] = {"name": username, "con": profilecon}
        data['current_users'][username] = {"name": username, "con": profilecon, "sessionid": sessionid}
        data['chat']['user'] = username
        data['chat']['message'] = ' {} 님이 입장하였습니다.'.format(username)
        data['chat']['profilecon'] = profilecon
        data['chat']['type'] = 'connect'
        data['chat']["sid"] = sessionid
    else:
        sessionid = request.sid
        message = message.replace("%20", " ")
        message = message.replace("%", "\\")
        message = message.encode('utf-8').decode('unicode_escape')
        myname = data['sessions'][sessionid]["name"]
        mycon = data['sessions'][sessionid]["con"]
        data['chat']['user'] = myname
        data['chat']['message'] = message
        data['chat']['profilecon'] = mycon
        data['chat']['type'] = 'normal'
    send(data, broadcast=True)

# @socket_io.on("leave")
# def on_leave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(data, room=room)


if __name__ == '__main__':
    socket_io.run(app, debug=True)

#jun test
