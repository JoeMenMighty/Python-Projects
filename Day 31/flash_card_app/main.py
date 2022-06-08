from tkinter import *
from tkinter import messagebox
from generate_word import generate_word, known_word

BACKGROUND_COLOR = "#B1DDC6"

new_word = {}


# change word function
def next_word():
    global new_word, timer
    window.after_cancel(timer)
    new_word = generate_word()
    card_canvas.itemconfig(background_img, image=front_card_img)
    card_canvas.itemconfig(card_title, text="French", fill='black')
    card_canvas.itemconfig(card_word, text=new_word['French'], fill='black')
    timer = window.after(3000, func=flip_card)


def flip_card():
    card_canvas.itemconfig(background_img, image=back_card_img)
    card_canvas.itemconfig(card_title, text="English", fill='white')
    card_canvas.itemconfig(card_word, text=new_word['English'], fill='white')


def remove_word():
    known_word(new_word)
    next_word()


# create window
window = Tk()
window.title("Mighty Flash Card App")
window.config(padx=40, pady=40, background=BACKGROUND_COLOR, highlightthickness=0)

# canvas for card
card_canvas = Canvas(width=810, height=530, highlightthickness=0, background=BACKGROUND_COLOR)
front_card_img = PhotoImage(file='images/card_front.png')
back_card_img = PhotoImage(file='images/card_back.png')
background_img = card_canvas.create_image(405, 265, image=front_card_img)
card_title = card_canvas.create_text(405, 150, text="", font=("Courier", 40, 'italic'))
card_word = card_canvas.create_text(405, 270, text="", font=("Courier", 60, 'bold'))
card_canvas.grid(column=0, row=0, columnspan=2)


# buttons for wrong and right
wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=remove_word)
right_button.grid(row=1, column=1)

timer = window.after(3000, func=flip_card)


next_word()

window.mainloop()