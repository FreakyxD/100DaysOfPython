import tkinter as tk
import time
from main import post_a_pixel


def on_enter_click():
    entered_value = entry.get()
    if entered_value.replace(".", "", 1).isdigit():
        success = False

        while not success:
            if post_a_pixel(entered_value) == 200:
                success = True
            time.sleep(1)

        # exit program
        root.after(1000, root.destroy)
    else:
        print("Please enter a valid number.")
    entry.delete(0, tk.END)


# Create the main Tkinter window
root = tk.Tk()
root.title("Habit Tracker")
root.config(padx=20, pady=20)

# Create and pack the headline label with larger font
headline_label = tk.Label(root, text="Habit Tracker", font=("Helvetica", 24))
headline_label.pack(pady=15)

# Create a label for the entry widget
hours_label = tk.Label(root, text="Hours today?", font=("Helvetica", 16))
hours_label.pack()

# Create and pack the entry widget for entering a float with larger font
entry = tk.Entry(root, width=5, font=("Helvetica", 18))
entry.pack(pady=10)
entry.focus()

# Create and pack the "Enter" button with larger font
enter_button = tk.Button(root, text="Enter", command=on_enter_click, font=("Helvetica", 18))
enter_button.pack(pady=15)

# Start the Tkinter event loop
root.mainloop()
