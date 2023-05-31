import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


# window
window = ttk.Window(themename='litera') # themename = 'journal, darkly, litera etc.
window.title('Miles to Kilometers')
window.geometry('500x270')

# function command
def convert():
    miles = entry_int.get()
    km = miles * 1.61
    output_label['text'] = km


# title label
title_lbl = ttk.Label(window, text='Miles to kilometers', font='Serif 24 bold')
title_lbl.pack(pady=10)

# input field
input_frame = ttk.Frame(window)

entry_int = tk.IntVar()
input_entry = ttk.Entry(input_frame, width=30, font='monospace 14 bold', textvariable=entry_int)
button = ttk.Button(input_frame, command=convert, text='Convert', bootstyle='primary-outline')

input_entry.pack(side='left', pady=5)
button.pack(side='left')
input_frame.pack()

# output label
output_label = ttk.Label(window, font='monospace 20 bold')
output_label.pack(pady=10)

window.mainloop()