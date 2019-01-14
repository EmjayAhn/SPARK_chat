from flask import Flask
from flask import render_template, url_for, request, redirect
from flask_socketio import SocketIO, send

app = Flask(__name__)
socket_io = SocketIO(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    global username, profilecon
    if request.method == 'POST':
        username = request.form['username']
        profilecon = request.form['profilecon']
        return render_template('chat.html', username=username, profilecon=profilecon)

@app.route("/chat")
def chat():
    return render_template('chat.html')

@socket_io.on("message")
def msg_send(message):
    global username, profilecon
    print("message : " + message)
    to_client = dict()
    if message == 'new_connect':
        to_client['message'] = '[{}]님이 입장하였습니다.'.format(username)
        to_client['profilecon'] = profilecon
        to_client['type'] = 'connect'
    else:
        to_client['message'] = username + ' : ' + message
        to_client['profilecon'] = profilecon
        to_client['type'] = 'normal'
    send(to_client, broadcast=True)


if __name__ == '__main__':
    app.run(debug=True)
    socket_io.run(app, debug=True)
