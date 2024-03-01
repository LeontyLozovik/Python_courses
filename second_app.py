import flask
from flask import Flask, request, redirect, render_template, send_from_directory, url_for
from werkzeug.utils import secure_filename
import os

BASE_DIR = os.getcwd()
app = Flask(__name__,
            static_folder=os.path.join(BASE_DIR, 'static'),
            template_folder=os.path.join(BASE_DIR, 'templates'))

app.config['SECRET_KEY'] = 'lLHBlhbljhbl&fvgv5ghkcy67bhHV'
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'uploads')
users = ['user1', 'user2', 'user3', 'user4']


@app.route('/')
def index():
    res = '<h4> ПОЛЬЗОВАТЕЛИ </h4>'
    for user in users:
        res += f'<p>Пользователь: {user}</p>'
    return res


@app.route('/favicon.ico/<string:mode>')
def favicon(mode):
    if mode == 's':
        return flask.send_file('static/img/favicon.ico', mimetype='image/jpg')
    elif mode == 'd':
        return flask.send_file('static/img/favicon.ico', as_attachment=True)
    else:
        return redirect('/')



@app.route('/users/')
def vew_users():
    return render_template('second_users.html', users=users, head='', color='red')


@app.route('/homeworks/<int:hid>')
def homeworks(hid):
    if hid == 1:
        return render_template('homework_1.html')
    else:
        return redirect('/')


@app.route('/homeworks/<int:hid>/<string:template_name>')
def homeworks_task(hid, template_name):
    return render_template(f'/homeworks/{hid}/{template_name}')


@app.route('/form1/', methods=['GET', 'POST'])
def form_get():
    if request.method == 'GET':
        return render_template('form1.html')
    file = request.files['file']
    if file:
        file_name = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
    return f'{request.form.get('name')}'


app.run(debug=True)
