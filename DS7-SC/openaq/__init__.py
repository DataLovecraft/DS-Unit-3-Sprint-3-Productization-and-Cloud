'''
Entry point for OpenAQ Flask Application
'''
from .aq_dashboard import create_app

APP = create_app()
