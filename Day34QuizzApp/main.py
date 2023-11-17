from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q_dict in question_data:
    # or question_bank.append(Question(q_dict["question"], q_dict["correct_answer"]))
    question_text = q_dict["question"]
    question_answer = q_dict["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

go_quiz = QuizBrain(question_bank)

while go_quiz.still_has_questions():
    go_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {go_quiz.score}/{go_quiz.question_number}")
