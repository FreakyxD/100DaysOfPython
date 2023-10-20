from tkinter import *

FONT = ("arial", 20)

# use radiobutton to choose conversion direction

# def radio_used():
#     print(radio_state.get())
#
#
# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

# Window
window = Tk()
window.title("Mile <> Kilometer Converter")
window.minsize(width=500, height=300)
window.maxsize(width=500, height=300)
window.config(padx=25, pady=25)

# Label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)
equal_label.config(padx=5, pady=5)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)
result_label.config(padx=5, pady=5)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)

# Entry
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# Button

window.mainloop()