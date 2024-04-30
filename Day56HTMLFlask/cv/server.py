from flask import Flask, render_template
app = Flask(__name__)

@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/")
def landing_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()