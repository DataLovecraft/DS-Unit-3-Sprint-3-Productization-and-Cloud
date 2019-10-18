'''
OpenAQ Air Quality Dashboard with Flask
'''
from decouple import config
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .models import DB, Record
from .openaq import openaq

def get_measurements(city='Los Angeles', parameter='pm25'):
    api = OpenAQ()
    status, body = api.measurements(city=city, parameter=parameter)
    return [{'utc_datetime': datetime.strptime(result['date']['utc'],
                                               '%Y-%m-%dT%H:%M:%S.%f%z'),
                                               'location': result['location'],
                                               'value': result['value']} for result in body['results']]

def create_app():
    '''
    Create and configure an instance of a flask application
    '''
    app = Flask(__name__)
    app.config['SQLAlCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)
    api = OpenAQ()

    @app.route('/')
    def root():
        '''
        Base View
        '''
        records = Record.query.filter(Record.value >= 10.0).all()
        return render_template('dash.html', title='', records=records)

    @app.route('/refresh')
    def refresh():
        '''
        Pull fresh data from OpenAQ and replace existing data
        '''
        DB.drop_all()
        DB.create_all()
        data = get_measurements()
        for record in data:
            DB.session.add(Record(utc_datetime=record['utc_datetime'],
                                  location=record['location'],
                                  value=record['value']))
        DB.session.commit()
        return 'Data refreshed!'
