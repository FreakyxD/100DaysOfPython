from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from sensitive import SECRET_KEY


class LoginForm(FlaskForm):
    username = StringField('username')
    password = StringField('password', validators=[DataRequired()])


app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():  # also needed for validating CSRF token
        username = login_form.username.data
        password = login_form.password.data
        print(username, password)
        # login logic
        return f"<h1>Login Successful for {username}</h1>"
    # for GET requests or if validation fails, render the form again
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
