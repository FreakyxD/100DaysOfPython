from tkinter import *

# Password generator

# Save Password
def save():
    # TODO warn if no data returned by any of the get()
    website = website_input.get()
    username = mail_user_input.get()
    password = password_input.get()

    with open("data.txt", mode="a") as file:
        file.write(f"{website} | {username} | {password}\n")

    reset_fields()

def reset_fields():
    website_input.delete(0, "end")
    password_input.delete(0, "end")

# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=1)
canvas.create_image(100, 100, image=logo)

# Label
sec_warning_label = Label(text="Do not use - insecure!", font=("Segoe UI", 20, "bold"), fg="red")
sec_warning_label.grid(column=1, row=0)
website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
mail_user_label = Label(text="Email/Username:")
mail_user_label.grid(column=0, row=3)
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

# Entry
website_input = Entry(width=35)
website_input.grid(column=1, row=2, columnspan=2)
website_input.focus()
mail_user_input = Entry(width=35)
mail_user_input.grid(column=1, row=3, columnspan=2)
mail_user_input.insert(0, "email@outlook.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=4)

# Button
password_btn = Button(text="New Password")
password_btn.grid(column=2, row=4)
add_btn = Button(text="Add", width=33, command=save)
add_btn.grid(column=1, row=5, columnspan=2)

window.mainloop()
