from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


def get_age():
    pass


def get_gender():
    pass


age = 22
gender = "female"


@app.route("/")
def landing_page():
    return "<h1 style='font-size: 30px'>Please go to /guess/yourname<h1>"


@app.route("/guess/<name>")
def guess(name):
    return render_template("guess.html", name=name.title(), age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
