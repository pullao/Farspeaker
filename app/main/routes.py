import flask
from . import main
from . import forms


@main.route('/', methods=['GET', 'POST'])
def index():
    """"Login form to enter a room."""
    form = forms.LoginForm()
    if form.validate_on_submit():
        flask.session['name'] = form.name.data
        flask.session['room'] = 'Default'
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
    return flask.render_template('chat.html', name=name)#, room=room)
