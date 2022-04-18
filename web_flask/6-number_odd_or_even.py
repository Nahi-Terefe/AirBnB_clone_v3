#!/usr/bin/python3
"""
a script that starts a Flask web application:
    - web application must be listening on 0.0.0.0, port 5000
    - Routes:
        * '/'
        * '/hbnb'
        * /c/<text>
        * /python/(<text>)
        * /number/<int:n>
        * /number_template/<int:n>
        * /number_odd_or_even/<int:n>
"""

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ returns 'hellow HBNB!' when GET root route """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ returns 'HBNB' when GET /hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def C_is_fun(text):
    """ returns 'C + text' what ever text
    passed when calling the route /c/<text>"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """
    display “Python ”, followed by the value of the text variable
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def is_it_number(n):
    """
    display “n is a number” only if n is an integer
    """
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def number_template(n):
    """
     display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """
    display a HTML page only if n is an integer.
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
