from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", css_url=url_for("static", filename="css/styles.css"),
                           js_url=(url_for("static", filename="js/scripts.js")))


if __name__ == "__main__":
    app.run(debug=True)
