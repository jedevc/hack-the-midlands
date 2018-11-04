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
    code = flask.request.args.get('code')

    db = get_db()
    result = db.get(code)
    if result:
        name, location = result
        image = '/api/images/' + code

        return flask.render_template('kitten.html', code=code, name=name,
                location=location, image=image)
    else:
        return '', 404
