class QuizBrain:

    def __init__(self, q_list):
        # ATTRIBUTES
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    # 3 METHODS
    def still_has_questions(self):
        # shorter version
        return self.question_number < len(self.question_list)

        # # Longer version
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    # Retrieve the item at the current question_number from the question_list.
    # Use the input( ) function to show the user the Question text and ask for the user's answer.
    def next_question(self):
        current_question = self.question_list[self.question_number]  # self.question_number will start at 0
        self.question_number += 1  # increase the question_number by 1 every time you call next_question
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print(f"The correct answer was: {correct_answer}.")
        print("\n")