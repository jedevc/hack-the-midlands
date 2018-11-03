from . import app, get_db

import flask
import os

@app.route('/')
def root():
    return flask.send_file('static/index.html')

@app.route('/api/codes/<string:code>')
def get_code(code):
    db = get_db()
    result = db.get(code)
    if result:
        name = result
        return flask.jsonify({
            'name': name,
            'image': '/api/images/' + code
        })
    else:
        return flask.jsonify({}), 404

@app.route('/api/images/<string:code>')
def get_image(code):
    db = get_db()
    result = db.getimage(code)
    if result:
        return flask.send_file(result)
    else:
        return ('', 404)
