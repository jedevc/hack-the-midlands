from . import app, get_db

import flask

@app.route('/api/kodes', methods = ['POST'])
def create_kode():
    params = flask.request.get_json()
    db = get_db()

    name = params['name']
    location = params['location']

    kode = db.create(name, location)
    image = '/api/images/' + kode

    return flask.jsonify({
        'kode': kode,
        'name': name,
        'image': image
    })

@app.route('/api/kodes/<string:kode>')
def get_kode(kode):
    db = get_db()
    result = db.get(kode)
    if result:
        name, location = result
        return flask.jsonify({
            'kode': kode,
            'name': name,
            'location': location,
            'image': '/api/images/' + kode
        })
    else:
        return flask.jsonify({}), 404

@app.route('/api/images/<string:kode>')
def get_image(kode):
    db = get_db()
    result = db.getimage(kode)
    if result:
        return flask.send_file(result)
    else:
        return '', 404
