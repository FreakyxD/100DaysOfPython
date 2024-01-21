from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>This is a paragraph.</p>"
            "<img src='https://media.giphy.com/media/v1"
            ".Y2lkPTc5MGI3NjExdm9scDRlYmVmd202dTkzenI0cXh6N25udjBrOHEzNmk0bGdjZjJwbCZlcD12MV9pbnRl"
            "cm5hbF9naWZfYnlfaWQmY3Q9Zw/KAq5w47R9rmTuvWOWa/giphy.gif'"
            "width=200>")


@app.route("/username/<name>/1")
def greet(name):
    return f"<p style='font-size: 200px'>Hello {name}!</p>"


@app.route("/math/add_ten/<int:number>")
def add_10(number):
    number += 10
    return f"{str(number)}"


if __name__ == "__main__":
    app.run(debug=True)
