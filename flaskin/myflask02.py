#!/usr/bin/python3

from flask import Flask, redirect, url_for

# Flask constructor takes the name of current module (__name__) as argument
app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return f'Hello admin!'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'Hello guest, {guest}'


@app.route('/hello/<name>')
def hello(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))
    

if __name__ == '__main__':
    app.run(port=5006)

