from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Save')