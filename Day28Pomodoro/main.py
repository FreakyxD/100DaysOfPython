from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(background=YELLOW, padx=100, pady=50)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# label
timer_label = Label(text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)
checkmark_label = Label(text="✔", background=YELLOW)
checkmark_label.grid(column=1, row=3)

# buttons
start_btn = Button(text="Start", highlightthickness=0)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", highlightthickness=0)
reset_btn.grid(column=2, row=2)

window.mainloop()
