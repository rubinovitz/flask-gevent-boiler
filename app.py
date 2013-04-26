import os
from flask import Flask, request, Response, render_template
import datetime
import logging
import os
import random
import re
import json
import jinja2
from socketio import socketio_manage
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
import redis 

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()
