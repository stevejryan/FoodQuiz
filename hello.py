""" 
"This hello.py file will serve as a minimal example of how to handle
HTTP requests. Inside it, you'll import the Flask object, and create 
a function that returns an HTTP response. Write the following code
inside hello.py: """

from flask import Flask

app = Flask(__name__)


@app.route('/')
# app.route() is a decorator that turns a regular Python function
# into a Flask _view function_, which converts the function's 
# return value into an HTTP response to be displayed by an HTTP
# client, such as a web browser
def hello():
    return 'Hello, World!'


# export FLASK_APP=hello