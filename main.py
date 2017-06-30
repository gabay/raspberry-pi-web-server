import os
import sys
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def main():
    app.run('127.0.0.1', 8000)


if __name__ == '__main__':
    main()
