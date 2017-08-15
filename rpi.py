import os
import sys
import time
import Queue
from flask import Flask, render_template, request, abort

app = Flask(__name__)

PAGES = [
    ('Home', '/'),
    ('Brandy', '/brandy'),
]
messages = Queue.Queue()


def render(page, **context):
    return render_template(page, pages=PAGES, **context)


@app.route('/')
def index():
    return render('index.html')


@app.route('/brandy')
def brandy():
    return render('brandy.html')


@app.route('/favicon.ico')
def favicon():
    return open(r'static/pi_logo.png', 'rb').read()


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        data = messages.get()
        print 'sending: "%s"' % data
        return data
    elif request.method == 'POST':
        print 'request data: "%s"' % request.data
        messages.put(request.data)
        return ''
    else:
        abort(401)


def main():
    host = sys.argv[1] if len(sys.argv) > 1 else ''
    port = sys.argv[2] if len(sys.argv) > 2 else 8000
    app.run(host, port, threaded=True)


if __name__ == '__main__':
    main()
