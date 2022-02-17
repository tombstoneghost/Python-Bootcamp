# Imports
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Question Bank
question_bank = []

for q in question_data:
    ques = Question(text=q["text"], answer=q["answer"])
    question_bank.append(ques)

# Start the Quiz
quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
