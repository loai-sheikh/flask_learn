from flask_wtf import Form
from wtforms import StringField, EmailField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError


class ContactForm(Form):
    name = StringField("Name of student", [
        validators.data_required("Please enter your name.")])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    address = TextAreaField("Address")

    email = EmailField("Email", [validators.data_required(
        'Please enter your email address.'), validators.Email('Please enter valid mail.')])
    age = IntegerField("Age")
    language = SelectField('Languages', choices=[
                           ('cpp', 'c++'), ('py', 'python')])
    submit = SubmitField("Send")
