from . import app, get_db

import flask

@app.route('/')
def root():
    return flask.render_template('index.html')

@app.route('/create')
def create_kitten():
    return flask.render_template('create.html')

@app.route('/kitten')
def view_kitten():
    kode = flask.request.args.get('kode')

    db = get_db()
    result = db.get(kode)
    if result:
        name, location = result
        image = '/api/images/' + kode

        return flask.render_template('kitten.html', kode=kode, name=name,
                location=location, image=image)
    else:
        return '', 404
