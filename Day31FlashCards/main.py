from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Load CSV
df = pd.read_csv("data/100_croatian_words.csv")
df.drop("Word Frequency", axis=1, inplace=True)
word_list = df.to_dict("records")
foreign_langauge = list(word_list[0].keys())[0]  # define foreign language depending on CSV data

# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load images
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# change later with canvas.itemconfig(lang_label, text="change")
lang_label = canvas.create_text(400, 150, text="language", font=("arial", 40, "italic"), fill="black")
word_label = canvas.create_text(400, 263, text="word", font=("arial", 60, "bold"), fill="black")

# Buttons
right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, height=97, width=97)
right_btn.grid(column=1, row=1)
wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0, height=97, width=97)
wrong_btn.grid(column=0, row=1)

window.mainloop()
