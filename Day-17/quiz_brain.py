class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_have_questions(self):
        return  self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number = self.question_number + 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score = self.score + 1
            print("You got it right.")
        else:
            print("That's wrong")
        
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")