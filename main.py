from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []  # This is where the object questions are stored.

for question in question_data:  # converts item from question_data into a Question object and place it
    # in question_bank
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
