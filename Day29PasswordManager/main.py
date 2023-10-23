from tkinter import *

# Password generator

# Save Password

# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=1)
canvas.create_image(100, 100, image=logo)

window.mainloop()
