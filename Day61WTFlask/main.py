from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length
from sensitive import SECRET_KEY


class LoginForm(FlaskForm):
    email = StringField('email', validators=[Email()])
    password = PasswordField('password', validators=[Length(min=14)])
    submit = SubmitField("Log In")


app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():  # also needed for validating CSRF token
        username = login_form.email.data
        password = login_form.password.data
        if username == "admin@email.com" and password == "11223344556677":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    # for GET requests or if validation fails, render the form again
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
