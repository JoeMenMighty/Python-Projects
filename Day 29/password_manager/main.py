from tkinter import *
from tkinter import messagebox
from password_genrator import generate_new_password
import pyperclip, json


# ----------------------------SEARCH BUTTON ------------------------------- #
def search():
    website_name = website_entry.get()

    try:
        with open('all_passwords.json', mode='r') as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showwarning(message="Sorry Your password list is empty. Please save a password first",
                               title="No Password Data File")
    else:
        if website_name in data.keys():
            searched_website = data[website_name]
            searched_email = searched_website['email']
            searched_password = searched_website['password']
            messagebox.showwarning(message=f"Email: {searched_email}\nPassword: {searched_password}",
                                   title=f"Search Result : {website_name}")
        else:
            messagebox.showwarning(message=f"Sorry there's no info for {website_name}",
                                   title=f"Search Result : {website_name}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    new_password = generate_new_password()
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)
    # pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # updated to json, makes json easier
    new_data = {
        website_name: {
            "email": email,
            "password": password,
        }
    }

    if len(website_name) == 0 or len(email) == 0 or len(password) == 0:
        message = f"You cannot leave any field empty"
        messagebox.showwarning(message=message, title="Check your entries")
    else:
        is_ok = messagebox.askokcancel(title="confirm save", message=f"Do you want to save these ?"
                                                                     f"\nWebsite : {website_name}"
                                                                     f"\nEmail : {email}"
                                                                     f"\nPassword : {password}")
        if is_ok:
            # with open('all_passwords.txt', mode='a') as password_file:
            #     entry_to_save = f"{website_name} | {email} | {password}\n"
            #     password_file.write(entry_to_save)

            # Updated to json format
            try:
                with open('all_passwords.json', mode='r') as password_file:
                    # load data in file
                    data = json.load(password_file)
            except FileNotFoundError:
                with open('all_passwords.json', mode='w') as password_file:
                    # save new data
                    json.dump(new_data, password_file, indent=4)
            else:
                # update data
                data.update(new_data)

                with open('all_passwords.json', mode='w') as password_file:
                    # save updated data
                    json.dump(data, password_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            # with open('all_passwords.json', mode='r') as password_file:
            #     # read json file and load data
            #     data = json.load(password_file)
            #
            #     # update the data
            #     data.update(new_data)
            #
            # # saving file
            # with open('all_passwords.json', mode='w') as password_file:
            #     json.dump(data, password_file, indent=4)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Mighty Password Manager")
# window.minsize(width=400, height=400)
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(110, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website label and entry
website_label = Label(text="Website : ")
website_label.config(pady=5)
website_label.grid(row=1, column=0)

website_entry = Entry(width=26)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=8, command=search)
search_button.grid(row=1, column=2)

# email label and entry
email_label = Label(text="Email : ")
email_label.config(pady=5)
email_label.grid(row=2, column=0)

email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'gob3deybee@gmail.com')

# password label and entry and button
password_label = Label(text="Password : ")
password_label.config(pady=5)
password_label.grid(row=3, column=0)

password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.grid(row=3, column=2)

# add password button
add_password_button = Button(text="Add", width=34, command=add_password)
add_password_button.config(pady=5)
add_password_button.grid(row=4, column=1, columnspan=2)


window.mainloop()