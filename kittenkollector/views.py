from . import app

import flask
import os

from robohash import Robohash

@app.route('/')
def root():
    return flask.send_file('static/index.html')

codes = {
    'foo': {
        'name': 'Foo kitten',
        'image': '/api/images/foo',
        'location': 'Hack the midlands'
    },
    'bar': {
        'name': 'Bar kitten',
        'image': '/api/images/bar',
        'location': 'Hack the midlands'
    }
}

@app.route('/api/codes/<string:code>')
def get_code(code):
    if code in codes:
        response = codes[code]
        return flask.jsonify(response)
    else:
        return flask.jsonify({}), 404

IMAGE_DIR='/tmp/kittenkollector/images/' 
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def find_image(code):
    path = '/tmp/kittenkollector/images/' + code + '.png'
    if not os.path.isfile(path):
        rh = Robohash(code)
        rh.assemble(roboset='set4')
        rh.img.save(path, 'png')

    return path

@app.route('/api/images/<string:code>')
def get_image(code):
    if code in codes:
        return flask.send_file(find_image(code))
    else:
        return ('', 404)
