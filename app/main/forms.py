import flask_wtf
import wtforms


class LoginForm(flask_wtf.Form):
    """Accepts a nickname and a room."""
    name = wtforms.fields.StringField('Name', validators=[wtforms.validators.Required()])
    #room = StringField('Room', validators=[Required()])
    submit = wtforms.fields.SubmitField('Start')
