from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_api_endpoint = "https://api.npoint.io/c1e867adbdc58198de7b"
response = requests.get(blog_api_endpoint)
response.raise_for_status()
blog_data = response.json()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
