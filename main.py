from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for index in range(len(question_data)):
    question_bank += [Question(question_data[index]["question"], question_data[index]["correct_answer"],
                               question_data[index]["category"], question_data[index]["difficulty"])]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.quiz_complete()
