from app import flask_app
import flask


@flask_app.route('/')
def index():
    return flask.render_template('index.html')


@flask_app.route("/register", method=("GET", "POST"))
def register():
    my_register_form = Form()
    if my_register_form.validate_on_submit():

        t_username = my_register_form.username.data
        t_password = my_register_form.password.data
        t_email = my_register_form.email.data

    else:

        return "Something went wrong", flask.redirect("/")

    return flask.render_template("profile.html", form=my_register_form)
