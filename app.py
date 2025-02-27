from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'
socketio = SocketIO(app)
host = '127.0.0.1:5000'

@app.route('/chat', methods=['GET'])
def chat():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)