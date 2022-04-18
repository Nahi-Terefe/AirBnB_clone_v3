#!/usr/bin/python3
"""
a basic Flask web application. with routes of
- '/' and '/hbnb'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ returns 'hellow HBNB!' when GET root route """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ returns 'HBNB' whe GET /hbnb """
    return 'HBNB'


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
