import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_age(input_name):
    response = requests.get(f"https://api.agify.io?name={input_name}")
    response.raise_for_status()
    return response.json()["age"]


def get_gender(input_name):
    response = requests.get(f"https://api.genderize.io?name={input_name}")
    response.raise_for_status()
    return response.json()["gender"]


@app.route("/")
def landing_page():
    return "<h1 style='font-size: 30px'>Please go to /guess/yourname<h1>"


@app.route("/guess/<name>")
def guess(name):
    age = get_age(name)
    gender = get_gender(name)
    return render_template("guess.html", person_name=name.title(), person_age=age, person_gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
