from tkinter import *
from tkcalendar import Calendar

root = Tk()
root.geometry('900x500+150+100')
root.title("Calendar")

# Create the calendar widget
cal = Calendar(root, selectmode='day', date_pattern='d/m/yy', height=500, width=500)
cal.pack(fill='both', expand=True)

root.mainloop()
