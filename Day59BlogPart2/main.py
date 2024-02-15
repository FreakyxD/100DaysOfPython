from flask import Flask, render_template
import requests

blog_api_endpoint = "https://api.npoint.io/c1e867adbdc58198de7b"
response = requests.get(blog_api_endpoint)
response.raise_for_status()
blog_data = response.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blogs=blog_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_number>")
def get_post(post_number):
    post_list_id = post_number - 1
    try:
        post_data = blog_data[post_list_id]
    # if the user is calling a blog number that doesn't exist
    except IndexError:
        return home()

    return render_template("post.html", post_data=post_data)


if __name__ == "__main__":
    app.run(debug=True)
