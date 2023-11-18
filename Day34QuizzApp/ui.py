from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # pass in a quiz_brain object, which is of data type QuizBrain
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas
        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)
        self.question_text = self.canvas.create_text(
            (150, 125),
            width=280,  # smaller than canvas to allow text wrap
            text="Question goes here",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)

        # Text field
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 20), fg="white")
        self.score_label.grid(column=1, row=0)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.quiz.check_answer("True")

    def false_pressed(self):
        self.quiz.check_answer("False")
