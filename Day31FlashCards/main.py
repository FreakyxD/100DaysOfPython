from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def card_memorized():
    word_list.remove(current_card)
    save_words_to_learn()
    next_card()


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(word_list)  # {'Croatian': 'me', 'English': 'me'}
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(lang_label, text=FOREIGN_LANGUAGE, fill="black")
    canvas.itemconfig(word_label, text=current_card[FOREIGN_LANGUAGE], fill="black")

    flip_timer = window.after(3000, func=flip_card)  # need to refresh timer duration


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(lang_label, text=NATIVE_LANGUAGE, fill="white")
    canvas.itemconfig(word_label, text=current_card[NATIVE_LANGUAGE], fill="white")

def save_words_to_learn():
    words_to_learn = pd.DataFrame(word_list)
    words_to_learn.to_csv(path_or_buf="words_to_learn.csv", index=False)


# Load CSV
try:
    df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/100_croatian_words.csv")
    df.drop("Word Frequency", axis=1, inplace=True)
finally:
    word_list = df.to_dict("records")
    # set languages based on CSV
    FOREIGN_LANGUAGE = list(word_list[0].keys())[0]
    NATIVE_LANGUAGE = list(word_list[0].keys())[1]

# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Load images
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263)
canvas.grid(column=0, row=0, columnspan=2)
lang_label = canvas.create_text(400, 150, text="", font=("arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("arial", 60, "bold"))

# Buttons
right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, height=97, width=97, command=card_memorized)
right_btn.grid(column=1, row=1)
wrong_btn = Button(image=wrong_img,highlightthickness=0, borderwidth=0, height=97, width=97, command=next_card)
wrong_btn.grid(column=0, row=1)

next_card()

window.mainloop()
