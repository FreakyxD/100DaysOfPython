from flask import Flask, render_template, request
import requests
from Day0UsefulCode.TelegramBot.main import TelegramBot

blog_api_endpoint = "https://api.npoint.io/e1461bef64973f02c2ff"
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


@app.route("/post/<int:post_number>")
def get_post(post_number):
    post_list_id = post_number - 1
    try:
        post_data = blog_data[post_list_id]
    # if the user is calling a blog number that doesn't exist
    except IndexError:
        return home()

    return render_template("post.html", post_data=post_data)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        received_message = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        telegram_bot = TelegramBot()
        print(received_message)
        telegram_bot.send_message_to_telegram_bot(message=received_message)

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run()
