from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global checkmarks
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", foreground=GREEN)
    checkmarks = ""
    checkmark_label.config(text=checkmarks)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """pass in an int in minutes"""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break+", foreground=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:  # even reps
        timer_label.config(text="Break", foreground=PINK)
        count_down(short_break_sec)
    else:  # uneven reps
        timer_label.config(text="Work", foreground=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global checkmarks
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks += "✔"
            checkmark_label.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(background=YELLOW, padx=100, pady=50)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# label
timer_label = Label(text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)
checkmark_label = Label(background=YELLOW, foreground=GREEN)
checkmark_label.grid(column=1, row=3)

# buttons
start_btn = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()
