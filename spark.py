from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

app.run()
