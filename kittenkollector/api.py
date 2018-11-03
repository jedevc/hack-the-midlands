from . import app, get_db

import flask

@app.route('/api/codes', methods = ['POST'])
def create_code():
    params = flask.request.get_json()
    db = get_db()

    name = params['name']
    code = db.create(name)
    image = '/api/images/' + code

    return flask.jsonify({
        'code': code,
        'name': name,
        'image': image
    })

@app.route('/api/codes/<string:code>')
def get_code(code):
    db = get_db()
    result = db.get(code)
    if result:
        name = result
        return flask.jsonify({
            'code': code,
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
        return '', 404
