import pandas
from turtle import Screen
import turtle

mighty_screen = Screen()
mighty_screen.title("Mighty's US State Game")
image = 'blank_states_img.gif'
mighty_screen.addshape(image)
turtle.shape(image)

all_answers = pandas.read_csv('50_states.csv')
all_states = all_answers['state'].to_list()
correct_answers = []

is_game_true = True

while is_game_true:
    answer_state = mighty_screen.textinput(title=f"{len(correct_answers)}/50 State name",
                                           prompt="Enter the name of the state")
    if answer_state.title() in all_states:
        correct_answers.append(answer_state.title())
        state_data = all_answers[all_answers.state == answer_state.title()]
        x_cord = int(state_data.x)
        y_cord = int(state_data.y)

        writer_turtle = turtle.Turtle()
        writer_turtle.hideturtle()
        writer_turtle.penup()
        writer_turtle.goto(x_cord, y_cord)
        writer_turtle.write(answer_state.title(), move=False, align='center', font=('courier', 9, 'normal'))

    if answer_state == 'exit':
        is_game_true = False

        missing_states = [state for state in all_states if (state not in correct_answers)]
        states_to_learn_df = pandas.DataFrame(missing_states)
        states_to_learn_df.to_csv('states_to_learn.csv')

# turtle.mainloop()