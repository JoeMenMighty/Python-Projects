from data import question_data, question_data_2
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
question_bank_2 = []

# loop through and create questions using question for question data for question bank
for _ in question_data:
    question_text = _['text']
    answer_text = _['answer']
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)

# loop through and create questions using question for question data for question bank
for _ in question_data_2:
    question_text = _['question']
    answer_text = _['correct_answer']
    new_question = Question(question_text, answer_text)
    question_bank_2.append(new_question)


# create the quiz
mighty_quiz = QuizBrain(question_bank_2)
has_questions = True

# check to see if questions are available then ask next question
while has_questions:
    mighty_quiz.next_question()
    has_questions = mighty_quiz.still_has_questions()

# display final score
final_score = mighty_quiz.current_score
total_answered = mighty_quiz.question_number

print(f"\nYou're done...!!!\nYour final score is {final_score}/{total_answered}")
if final_score > 6:
    print("congratulations!!!!!!!!!!!!! You passed.........")
else:
    print("Sorry....You failed.... Better luck next time")
