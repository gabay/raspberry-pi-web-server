import os
import sys
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def main():
    host = sys.argv[1] if len(sys.argv) > 1 else ''
    port = sys.argv[2] if len(sys.argv) > 2 else 8000
    app.run(host, port)


if __name__ == '__main__':
    main()
