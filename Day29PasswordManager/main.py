from tkinter import *
from tkinter import messagebox
from passwordgenerator import generate_password
import json


def handle_password():
    password_input.delete(0, "end")
    password_input.insert(0, generate_password())


def save_json(data):
    with open("data.json", mode="w") as file:
        json.dump(data, file, indent=4)


# Save Password
def save():
    website = website_input.get()
    username = mail_user_input.get()
    password = password_input.get()
    data_dict = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                # reading old data
                data = json.load(file)  # creates a python dictionary
        except FileNotFoundError:
            save_json(data_dict)
        else:
            # updating old data with new data
            data.update(data_dict)
            save_json(data)
        finally:
            reset_fields()


def reset_fields():
    website_input.delete(0, "end")
    password_input.delete(0, "end")


def find_password():
    search_term = website_input.get()
    if website_input.get() == "":
        messagebox.showwarning(title="Oops", message="Please fill the website field!")
    else:
        with open("data.json", mode="r") as file:
            try:
                data = json.load(file)
            except FileNotFoundError:
                messagebox.showwarning(title="Warning", message="No saved passwords found!")
            else:
                if search_term in data:
                    email = data[search_term]["email"]
                    password = data[search_term]["password"]
                    messagebox.showinfo(title="Search Result", message=f"Email: {email}\nPassword: {password}")
                else:
                    messagebox.showwarning(title="Warning", message=f"No entry for '{search_term}' found.")


# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=1)
canvas.create_image(100, 100, image=logo)

# Label
sec_warning_label = Label(text="Do not use - insecure!", font=("Segoe UI", 20, "bold"), fg="#CF382B")
sec_warning_label.grid(column=1, row=0)
website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
mail_user_label = Label(text="Email/Username:")
mail_user_label.grid(column=0, row=3)
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

# Entry
website_input = Entry(width=21)
website_input.grid(column=1, row=2)
website_input.focus()
mail_user_input = Entry(width=35)
mail_user_input.grid(column=1, row=3, columnspan=2)
mail_user_input.insert(0, "email@outlook.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=4)

# Button
search_btn = Button(text="Search", width=10, command=find_password)
search_btn.grid(column=2, row=2)
password_btn = Button(text="New Password", command=handle_password)
password_btn.grid(column=2, row=4)
add_btn = Button(text="Add", width=33, command=save)
add_btn.grid(column=1, row=5, columnspan=2)

window.mainloop()
