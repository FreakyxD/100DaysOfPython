from tkinter import *

# Password generator

# Save Password

# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)
canvas.create_image(100, 100, image=logo)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
mail_user_label = Label(text="Email/Username:")
mail_user_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
mail_user_input = Entry(width=35)
mail_user_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Button
password_btn = Button(text="New Password")
password_btn.grid(column=2, row=3)
add_btn = Button(text="Add", width=33)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
