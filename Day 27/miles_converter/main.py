from tkinter import *

# creating new window
new_window = Tk()
new_window.title("Mighty's Mile converter")
new_window.minsize(width=500, height=300)
new_window.config(padx=50, pady=50)


# create labels and buttons and entrys
def convert():
    mile_distance = int(val_convert.get())
    km_distance = 1.609 * mile_distance
    converted_val_label.config(text=f'{km_distance}')


is_equal_to_label = Label(text="Is Equal to")
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=20, pady=20)

converted_val_label = Label(text='0')
converted_val_label.grid(column=1, row=1)
converted_val_label.config(padx=20, pady=20)

val_convert = Entry(width=15)
val_convert.insert(END, string='Enter mile Value')
val_convert.grid(column=1, row=0)

# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# scales = ["miles", "kilometer", "meter", 'centimeter']
# for item in scales:
#     listbox.insert(scales.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.grid(column=2, row=0)


scale_from_label = Label(text='miles')
scale_from_label.grid(column=2, row=0)
scale_from_label.config(padx=20, pady=20)

scale_to_label = Label(text='km')
scale_to_label.grid(column=2, row=1)
scale_to_label.config(padx=20, pady=20)

calculate_button = Button(text="convert", command=convert)
calculate_button.grid(column=1, row=2)



new_window.mainloop()
