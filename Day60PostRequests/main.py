from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def receive_data():
    error = None
    if request.method == "POST":
        print(request.form["username"])
        print(request.form["password"])
    return "Login ok"


if __name__ == "__main__":
    app.run()
