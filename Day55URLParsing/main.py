from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        input_string = function()
        formatted_string = f"<b>{input_string}</b>"
        return formatted_string

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        input_string = function()
        formatted_string = f"<em>{input_string}</em>"
        return formatted_string

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        input_string = function()
        formatted_string = f"<u>{input_string}</u>"
        return formatted_string

    return wrapper_function


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


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"


@app.route("/math/add_ten/<int:number>")
def add_10(number):
    number += 10
    return f"{str(number)}"


if __name__ == "__main__":
    app.run()
