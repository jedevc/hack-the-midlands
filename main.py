import flask
from flask import Flask

import os

from robohash import Robohash

app = Flask(__name__)

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

def find_image(code):
    path = 'images/' + code + '.png'
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
        return flask.send_file(find_image(code))
        return ('', 404)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
