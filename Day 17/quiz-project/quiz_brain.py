class QuizBrain:

    def __init__(self, questions):
        self.question_list = questions
        self.question_number = 0
        self.current_score = 0

    def still_has_questions(self):
        has_questions = True
        if self.question_number >= len(self.question_list):
            has_questions = False
        return has_questions
        # return self.question_number >= len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"\nQ.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(player_answer, current_question.answer)

    def check_answer(self, player_choice, correct_answer):
        if player_choice.lower() == correct_answer.lower():
            print("You're right...!!!")
            self.current_score += 1
        else:
            print("You're wrong...!!!")
        print(f"The correct answer is {correct_answer.title()} "
              f"\nYour current score is : {self.current_score}/{self.question_number}")

