import flask
from flask import Flask

from .database import Database

app = Flask(__name__)

DATABASE = 'kittens.db'

def get_db():
    db = getattr(flask.g, '_database', None)
    if not db:
        db = flask.g._database = Database(DATABASE)
    return db

@app.teardown_appcontext
def close_db(exception):
    db = getattr(flask.g, '_database', None)
    if db:
        db.close()

import kittenkollector.views
