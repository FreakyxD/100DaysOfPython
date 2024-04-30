import requests
from post import Post
from flask import Flask, render_template

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
all_posts = response.json()

post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", post_objects=post_objects)


@app.route("/post/<int:num>")
def get_blog(num):
    requested_post = None
    for post_obj in post_objects:
        if post_obj.id == num:
            requested_post = post_obj
    return render_template("post.html", post_obj=requested_post, blog_id=num)


if __name__ == "__main__":
    app.run()
