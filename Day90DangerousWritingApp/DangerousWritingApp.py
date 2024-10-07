import tkinter as tk
from threading import Timer


class DangerousWritingApp:
    def __init__(self, tk_root):
        self.root = tk_root
        self.root.title("Dangerous Writing App")

        self.textbox = tk.Text(self.root, wrap='word', font=("Helvetica", 14))
        self.textbox.pack(expand=True, fill='both')

        self.textbox.bind('<KeyRelease>', self.reset_timer)

        self.timer = None
        self.timeout_seconds = 5

    def start_timer(self):
        self.timer = Timer(self.timeout_seconds, self.clear_text)
        self.timer.start()

    def reset_timer(self, event):
        if self.timer is not None:
            self.timer.cancel()
        self.start_timer()

    def clear_text(self):
        self.textbox.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
