class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def next_question(self):
        current_q_num = self.question_number
        current_ques = self.question_list[current_q_num]
        user_ans = input(f"Q.{current_q_num + 1}: {current_ques.text}.(True/False)?: ")
        self.check_answer(user_ans, current_ques.answer)


    def still_has_questions(self):
        return self.question_number <= (len(self.question_list)-1)


    def check_answer(self, user_ans, corresct_ans):
        if user_ans.lower() == corresct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {corresct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print("\n")


