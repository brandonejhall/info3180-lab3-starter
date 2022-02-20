from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateTimeLocalField,EmailField,SelectField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    subject = StringField('Subject',validators=[DataRequired()])
    message = StringField('Message',validators=[DataRequired()])
    submit = SubmitField('Submit')
