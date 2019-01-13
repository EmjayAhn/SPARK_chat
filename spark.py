from flask import Flask
from flask import render_template, url_for, request, redirect
from flask_socketio import SocketIO, send

app = Flask(__name__)
socket_io = SocketIO(app)

@app.route("/")
def home():

    return render_template('index.html')

# @app.route("/chat")
# def chat():
# 	# animal = "dog"
#     return render_template('chat.html', value="eunice", img="picture")
#
# @app.route("/chat", methods=['POST'])
# def payment():
# 	return render_template('index.html', value=animal)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        id = request.form['user_id']
        return render_template('chat.html', id=id)
#
@socket_io.on("message")
def msg_new(message):
    print("message : " + message)
    to_client = dict()
    if message == 'new_connect':
<<<<<<< HEAD
        to_client['message'] = '[{}]님이 입장하였습니다.'.format(user_id)
=======
        to_client['message'] = '가 입장하였습니다.'
>>>>>>> Feat: index and chat connected
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'
    send(to_client, broadcast=True)


if __name__ == '__main__':
	app.run(debug=True)
	socket_io.run(app, debug=True)
