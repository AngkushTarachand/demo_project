import flask_wft
import wtforms


class Form(flask_wft.FlaskForm):
    username = wtforms.StringField("Name")
    email = wtforms.StringField("Email")
    password = wtforms.PasswordField("Password")
    submit = wtforms.Submit("Submit")


