class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, current_question_answer):
        if user_answer.lower() == current_question_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"the correct answer was: {current_question_answer}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Category: {current_question.category}")
        print(f"Difficulty: {current_question.difficulty}")
        user_answer = input(f"Q.{self.question_number}: {current_question.text}(True/False): ")
        current_question_answer = current_question.answer
        self.check_answer(user_answer, current_question_answer)
        print(f"current score: {self.score}/{self.question_number}")
        print("\n")

    def quiz_complete(self):
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}")
