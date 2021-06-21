import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run()