import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageFont, ImageDraw

# Root window setup
root = tk.Tk()
root.title('Add a Watermark')
root.resizable(True, True)

# Global variables
img = None
img_path = None
tk_image = None  # To keep the image reference
MY_WATERMARK = "©Company"

# UI Elements
image_label = tk.Label(root)
image_label.pack(pady=10, padx=20)

label = ttk.Label(root, text="Please choose a picture below...")
label.pack(pady=(10, 5), padx=20)

operation_button = ttk.Button(root, text="Add an Image", command=lambda: select_image())
operation_button.pack(pady=10, padx=20)


def select_image():
    global img, img_path, tk_image
    img_path = fd.askopenfilename(filetypes=[("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg")])

    if img_path:
        img = Image.open(img_path)
        img_thumbnail = img.resize((128, 128), Image.Resampling.LANCZOS)
        preview_image(img_thumbnail)


def preview_image(img_thumbnail):
    global tk_image
    tk_image = ImageTk.PhotoImage(img_thumbnail)
    image_label.config(image=tk_image)
    swap_button(action="watermark")


def add_watermark():
    global img
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("Helvetica", 150)
    except IOError:
        font = ImageFont.load_default()

    draw.text((20, 20), MY_WATERMARK, fill=(255, 255, 255), font=font)
    save_file(img)


def save_file(img_watermarked):
    filename = fd.asksaveasfilename(defaultextension=".jpg")
    if filename:
        img_watermarked.save(filename)
        swap_button(action="select_image")


def swap_button(action):
    if action == "watermark":
        operation_button.config(text="Add watermark & Save", command=add_watermark)
    elif action == "select_image":
        operation_button.config(text="Add an Image", command=select_image)


root.mainloop()
