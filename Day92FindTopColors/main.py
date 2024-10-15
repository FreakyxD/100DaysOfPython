import os
from PIL import Image

from flask import Flask, render_template, redirect, request, flash, url_for
from werkzeug.utils import secure_filename
from sensitive import SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(file_to_check):
    return "." in file_to_check and file_to_check.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def upload_page():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if request.files["file"].filename == "":
        flash("Please select a file to be uploaded")
        return redirect(url_for("upload_page"))
    file = request.files["file"]
    if file and allowed_file(file.filename):
        file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(file_path)
        return redirect(url_for('results', filename=file.filename))
    return "Invalid file type", 400


@app.route("/results")
def results():
    filename_received = request.args.get("filename")
    if filename_received:
        file_path = os.path.join(UPLOAD_FOLDER, filename_received)
        list_of_top_colors = get_dominant_colors(file_path)

        colors_list = [{"Color": color[0], "Percentage": "{:.2f}".format(color[1])} for color in list_of_top_colors]

        return render_template('colors.html', colors=colors_list)
    return "No file provided", 400


def get_dominant_colors(file_path, palette_size=16, num_colors=10):
    # Resize image to speed up processing
    img = Image.open(file_path)
    img.thumbnail((100, 100))

    # Reduce colors (uses k-means internally)
    paletted = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=palette_size)

    # Get the color palette and count how often each color appears
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)

    total_pixels = sum([count for count, _ in color_counts])

    dominant_colors = []
    for i in range(min(num_colors, len(color_counts))):
        count, palette_index = color_counts[i]
        rgb = palette[palette_index * 3:palette_index * 3 + 3]
        hex_val = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
        percentage = (count / total_pixels) * 100
        dominant_colors.append((hex_val, percentage))

    return dominant_colors


if __name__ == "__main__":
    app.run(port=5002)
