import os
import sys
import time

from flask import Flask, render_template, request, abort
from flask_socketio import SocketIO, emit

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'qjr39d66n3a9_!g7#'
socketio = SocketIO(app)

PAGES = [
    ('Home', '/'),
    ('Brandy', '/brandy'),
    ('Chat', '/chat'),
    ('TicTacToe', '/tictactoe'),
]


def render(page, **context):
    return render_template(page, pages=PAGES, **context)


@app.route('/')
def index():
    return render('index.html')


@app.route('/favicon.ico')
def favicon():
    return open(r'static/pi_logo.png', 'rb').read()


@app.route('/brandy')
def brandy():
    return render('brandy.html')


@app.route('/chat')
def chat():
    return render('chat.html')


@app.route('/tictactoe')
def tictactoe():
    return render('tictactoe.html')


@socketio.on('message', namespace='/chat/io')
def chat_message(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    final_message = message['message']
    if message['user']:
        final_message = '%s: %s' % (message['user'], final_message)
    emit('message', {'message': final_message}, broadcast=True)


def main():
    host = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0'
    port = sys.argv[2] if len(sys.argv) > 2 else 8000
    socketio.run(app, host, port)


if __name__ == '__main__':
    main()
