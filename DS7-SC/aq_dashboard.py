'''
OpenAQ Air Quality Dashboard with Flask
'''

from flask import flask

APP = Flask(__name__)

@APP.route('/')
def root():
    '''
    Base View
    '''
    return 'TODO - part 2 and beyond!'
