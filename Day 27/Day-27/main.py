from tkinter import *

LABEL_FONT = ('courier', 15, 'normal')
BUTTON_FONT = ('courier', 9, 'normal')

# creating a new window
window = Tk()
window.title("Mighty's first GUI Application")
window.minsize(width=500, height=400)

# creating a label
label = Label(text='New Label', font=LABEL_FONT)
label.grid(column=0, row=0)

click_times = 0
# creating a button

# FUNCTION FOR BUTTON CLICK
# def button_click():
#     global click_times
#     click_times += 1
#     label.config(text=f'Clicked {click_times}')
#     # print('I got clicked!!!')


def button_click():
    user_entry = entry.get()
    label.config(text=user_entry)


button = Button(text='Click Me', command=button_click, font=BUTTON_FONT)
button.grid(column=1, row=1)

button = Button(text='Click Me 2', command=button_click, font=BUTTON_FONT)
button.grid(column=2, row=0)

# creating an entry
entry = Entry(width=15)
entry.grid(column=3, row=3)







window.mainloop()

