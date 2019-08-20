#!/usr/bin/python3

#An object of Flask class is our WSGI application
from flask import Flask
#Flask constructor takes the name of current module (__name__) as argument
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    with open('helloworld.txt', 'w') as hello:
        hello.write('You just wrote this line into helloworld.txt')
    return 'File created'

@app.route('/goodbye/')
def goodbye_world():
    with open('goodbye.world', 'w') as goodbye:
        goodbye.write('Later my dudes!')
    return 'File created'

if __name__ == '__main__':
    app.run(port=5006) # runs the application
    # app.run(port=5006, debug=True) # DEBUG MODE


