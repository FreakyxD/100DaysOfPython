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
window.config(padx=25, pady=25)

# Label
convert_choice_label = Label(text="Convert to:", font=FONT)
convert_choice_label.grid(column=0, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=2)
miles_label.config(padx=5, pady=5)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=3)
equal_label.config(padx=5, pady=5)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=3)
result_label.config(padx=5, pady=5)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=3)
km_label.config(padx=5, pady=5)

# Radio
radio_state = IntVar()  # Variable to hold on to which radio button value is checked

radiobutton1 = Radiobutton(text="Miles", value=1, variable=radio_state, command=radio_used)
radiobutton1.grid(column=1, row=0)

radiobutton2 = Radiobutton(text="Km", value=2, variable=radio_state, command=radio_used)
radiobutton2.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
user_input.grid(column=1, row=2)

# Empty grid row
empty_label = Label(text="")
empty_label.grid(column=0, row=1)

# Button
calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=4)

window.mainloop()
