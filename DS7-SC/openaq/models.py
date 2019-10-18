'''
SQLAlchemy models for OpenAQ APP
'''
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    country = DB.Column(DB.String(2))
    city = DB.Column(DB.String(25))
    location = DB.Column(DB.Text)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return "<Record (country='{}', city='{}', location='{}', datetime='{}', value='{}')>".format(self.country, self.city, self.location, self.datetime, self.value)
