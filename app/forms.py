import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    username = wtforms.StringField("Name")
    email = wtforms.StringField("Email")
    password = wtforms.PasswordField("Password")
    submit = wtforms.SubmitField("Submit")
