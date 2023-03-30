import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")

        # Create a text widget to display and edit text
        self.text = tk.Text(master)
        self.text.pack(expand=True, fill=tk.BOTH)

        # Create a menu bar with 'File' menu
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)
        
        #create anothers menu bar 
        edit = tk.Menu(menubar, tearoff=0)
        edit.add_command(label="Cut")
        edit.add_command(label="Copy")
        edit.add_command(label="Font")
        edit.add_command(label="Size")
        menubar.add_cascade(label="Edit", menu=edit)
        master.config(menu=menubar)
        
        #another
        help = tk.Menu(menubar, tearoff=0)
        help.add_command(label="About")
        help.add_command(label="Contact me")
        help.add_command(label="Information")
        help.add_command(label="Report")
        menubar.add_cascade(label="Help", menu=help)
        master.config(menu=menubar)

        # Set initial file path to None
        self.file_path = None

    def new_file(self):
        self.text.delete('1.0', tk.END)  # Clear the text widget
        self.file_path = None  # Reset the file path

    def open_file(self):
        file_path = filedialog.askopenfilename()  # Open file dialog to choose file to open
        if file_path:
            with open(file_path, 'r') as file:
                file_content = file.read()  # Read the file content
                self.text.delete('1.0', tk.END)  # Clear the text widget
                self.text.insert('1.0', file_content)  # Insert the file content into the text widget
                self.file_path = file_path  # Set the file path

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text.get('1.0', tk.END))  # Write the text widget content to file
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')  # Open file dialog to choose file to save
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text.get('1.0', tk.END))  # Write the text widget content to file
                self.file_path = file_path  # Set the file path

root = tk.Tk()
editor = TextEditor(root)
root.mainloop()
