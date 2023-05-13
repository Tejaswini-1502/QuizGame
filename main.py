from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    obj_ques = Question(question["question"], question["correct_answer"])
    question_bank.append(obj_ques)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    quiz.question_number += 1

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}.")