from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Email, InputRequired


class ContactForm(FlaskForm):
    name = StringField("Name: ", validators=[InputRequired()])
    email = StringField("Email: ", validators=[InputRequired(), Email()])
    message = TextAreaField("Message", validators=[InputRequired()])
    submit = SubmitField("Submit")
