from tkinter import *
from tkinter import messagebox
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    pomodoro_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- # 
# start count function
def start_counter():

    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 == 1 and reps == 7:
        count_down(long_break)
        color_ = RED
        status = f"Long Break"
        messagebox.showinfo(title=status, message=f"It's {status} time")
    elif reps % 2 == 1:
        count_down(short_break)
        color_ = PINK
        status = f"Short Break"
        messagebox.showinfo(title=status, message=f"It's {status} time")
    elif reps % 2 == 0:
        count_down(work_time)
        color_ = GREEN
        status = f"Work"
        messagebox.showinfo(title=status, message=f"It's {status} time")

    pomodoro_label.config(text=status, fg=color_)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_mins = math.floor(count / 60)
    count_sec = count % 60

    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps, check_count
        reps += 1

        if reps % 2 == 0:
            check_count += 1
            check_status = "✓" * check_count
            check_label.config(text=check_status)
        start_counter()


# ---------------------------- UI SETUP ------------------------------- #

# window to display pomodoro
window = Tk()
window.title("Mighty's Pomodoro Timer")
window.minsize(width=400, height=300)
window.config(padx=100, pady=50, bg=YELLOW)


# labels on top of pomodoro
pomodoro_label = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
pomodoro_label.grid(column=1, row=0)


check_label = Label(text="", font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

# canvas to contain pomodoro image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)


# buttons for pomodoro
start_button = Button(text='start', command=start_counter)
start_button.grid(column=0, row=2)


reset_button = Button(text='reset', command=reset)
reset_button.grid(column=2, row=2)




window.mainloop()