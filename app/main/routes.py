import flask
from . import main
from . import forms
import os
from werkzeug import secure_filename
from flask import Flask, render_template, request
from . import activeCampaign




@main.route('/', methods=['GET', 'POST'])
def index():
    """"Login form to enter a room."""
    form = forms.LoginForm()
    if form.validate_on_submit():
        flask.session['name'] = form.name.data
        flask.session['room'] = 'main'
        return flask.redirect(flask.url_for('.chat'))
    elif flask.request.method == 'GET':
        form.name.data = flask.session.get('name', '')
        #form.room.data = session.get('room', '')
    return flask.render_template('index.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = flask.session.get('name', '')
    room = flask.session.get('room', '')
    if name == '' or room == '':
        return flask.redirect(flask.url_for('.index'))
    return flask.render_template('chat.html', name=name, campaign=activeCampaign)#, room=room)

app=Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@main.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      if f:
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return flask.render_template('chat.html')