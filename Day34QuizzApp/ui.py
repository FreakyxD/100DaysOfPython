from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas
        canvas = Canvas(height=250, width=300)
        canvas.grid(column=0, row=1, columnspan=2, pady=20)
        question_text = canvas.create_text((150, 125), text="Question goes here", font=("Arial", 20, "italic"))

        # Text field
        score_label = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 20), fg="white")
        score_label.grid(column=1, row=0)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        true_btn = Button(image=true_img)
        true_btn.grid(column=0, row=2, pady=20)
        false_btn = Button(image=false_img)
        false_btn.grid(column=1, row=2)



        self.window.mainloop()
