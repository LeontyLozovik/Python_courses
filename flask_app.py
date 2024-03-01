import os
import flask
from flask import Flask, render_template

BASE_DIR = os.getcwd()
app = Flask(__name__,
            static_folder=os.path.join(BASE_DIR, 'static'),
            template_folder=os.path.join(BASE_DIR, 'templates'))


@app.route('/')
def index():
    return render_template('homework.html')


@app.route('/favicon.ico')
def favicon():
    with open('app/static/img/favicon.ico', 'rb') as icon:
        return icon.read()


@app.route('/users/', methods=['GET'])
def get_users():
    return render_template('users.html')


@app.route('/cites/')
def get_cites():
    return render_template('cites.html')


@app.route('/<string:filename>')
def get_file(filename):
    if filename[-4:] in ['.jpg', '.png', '.gif']:
        return flask.send_file(f'static/img/{filename}', mimetype='image/jpg')
    elif filename[-4:] == '.zip':
        return flask.send_file(f'static/zip/{filename}', mimetype='application/zip')
    else:
        flask.abort(404)


@app.route('/cat/<int:id>')
def cat(id):
    return f'Hello from {id} cat'


app.run(debug=True)
