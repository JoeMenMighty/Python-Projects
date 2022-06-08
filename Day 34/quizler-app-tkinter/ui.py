from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Mighty Quiz")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text=f"Score  :  {self.quiz.score}", bg=THEME_COLOR, fg="White")
        self.score_label.grid(row=0, column=1)

        self.question_box_canvas = Canvas(width=300, height=250)
        self.question_box_canvas_text = self.question_box_canvas.create_text(
            150,
            125,
            width=290,
            text='Questions',
            fill=THEME_COLOR,
            font=("Arial", 20, 'italic')
        )
        self.question_box_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img, highlightthickness=0, padx=20, pady=20, command=self.true_check)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, padx=20, pady=20, command=self.false_check)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_box_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score  :  {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_box_canvas.itemconfig(self.question_box_canvas_text, text=q_text)
        else:
            self.question_box_canvas.itemconfig(self.question_box_canvas_text,
                                                text=f"You've reached the end of the quiz\n"
                                                     f"You scored {self.quiz.score} / {len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_check(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_check(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_box_canvas.config(bg="green")
        else:
            self.question_box_canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


