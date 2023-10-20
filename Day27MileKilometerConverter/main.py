from tkinter import *

FONT = ("arial", 20)


def convert():
    n = float(user_input.get())
    result = round(n * 1.609344, 2)
    result_label.config(text=result)


def radio_used():
    print(radio_state.get())


# Window
window = Tk()
window.title("Mile > Kilometer Converter")
window.minsize(width=350, height=175)
window.maxsize(width=350, height=175)
window.config(padx=25, pady=25)

# Label
convert_choice_label = Label(text="Convert to:", font=FONT)
convert_choice_label.grid(column=0, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=1)
miles_label.config(padx=5, pady=5)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=2)
equal_label.config(padx=5, pady=5)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=2)
result_label.config(padx=5, pady=5)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=2)
km_label.config(padx=5, pady=5)

# Radio
radio_state = IntVar()  # Variable to hold on to which radio button value is checked

radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton1.grid(column=1, row=0)

radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton2.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
user_input.grid(column=1, row=1)

# Button
calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=3)

window.mainloop()
