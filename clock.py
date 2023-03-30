import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self, master):
        self.master = master
        master.title("Digital Clock")

        # Create label widget to display the time
        self.time_label = tk.Label(master, font=('Arial', 30), fg='black', bg='skyblue')
        self.time_label.pack(pady=50, padx=50)

        # Update the time every 200 milliseconds
        self.update_time()

    def update_time(self):
        current_time = strftime('%H:%M:%S %p')  # Get the current time in the format HH:MM:SS AM/PM
        self.time_label.config(text=current_time)  # Update the time label with the current time
        self.master.after(200, self.update_time)  # Schedule the next update after 200 milliseconds

root = tk.Tk()
clock = DigitalClock(root)
root.mainloop()
