from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import csv
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('dbUrl')
db = SQLAlchemy(app)


