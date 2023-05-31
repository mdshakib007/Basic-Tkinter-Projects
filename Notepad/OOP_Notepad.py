from tkinter import *
from tkinter import messagebox, colorchooser, font, filedialog
import os


class NotePaaD:
    def __init__(self, master):  # initial constractor to pass 'root' as master
        self.master = master
        self.file = None
        master.title('Untitled   -   NotePaaD')
        master.geometry('888x555')
        master.minsize(444, 233)

        # create the text area
        self.text_area = Text(master, undo=True, fg='black',
                              bg='white', font='Arial 14')
        self.text_area.pack(fill=BOTH, expand=True)

        # define the vertical scroller
        scroll = Scrollbar(self.text_area)
        scroll.pack(side='right', fill='y')
        scroll.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=scroll.set)

        # create the menubar's
        self.main_menu = Menu(master)  # main horizontal menu

        # first main vertical menu
        self.m1 = Menu(self.main_menu, tearoff=0)
        self.m1.add_command(label='New Text File', command=self.new_text_file)
        self.m1.add_command(label='New File...', command=self.new_file)
        self.m1.add_command(label='Open File', command=self.open_file)
        self.m1.add_command(label='Open Recent', command=self.recent)
        self.m1.add_separator()
        self.m1.add_command(label='Save', command=self.save)
        self.m1.add_command(label='Save As...', command=self.save_as)
        self.m1.add_command(label='Save All', command=self.save_all)
        self.m1.add_separator()
        self.m1.add_command(label='Share', command=self.share)
        self.m1.add_separator()
        self.m1.add_command(label='Exit', command=master.destroy)

        self.main_menu.add_cascade(label='File', menu=self.m1)

        # second main vertical menu
        self.m2 = Menu(self.main_menu, tearoff=0)
        self.m2.add_command(label='Undo', command=self.undo)
        self.m2.add_command(label='Redo', command=self.redo)
        self.m2.add_separator()
        self.m2.add_command(label='Cut', command=self.cut)
        self.m2.add_command(label='Copy', command=self.copy)
        self.m2.add_command(label='Paste', command=self.paste)
        self.m2.add_separator()
        self.m2.add_command(label='Resize Editor', command=self.resize)
        self.m2.add_command(label='Expand Editor', command=self.expand)
        self.m2.add_separator()
        self.m2.add_command(label='Close', command=quit)

        self.main_menu.add_cascade(label='Edit', menu=self.m2)
        master.config(menu=self.main_menu)

        # this is third main vertical menu
        self.m3 = Menu(self.main_menu, tearoff=0)

        self.m3.add_command(label='Change Background', command=self.change_bg)
        self.m3.add_command(label='Font Color', command=self.font_color)
        self.m3.add_separator()
        # this is sub main menu of font
        self.font_menu = Menu(self.m3, tearoff=0)
        self.font_menu.add_command(label='Arial (Default)',
                                   command=lambda: self.select_font('Arial'))
        self.font_menu.add_command(label='Calibri',
                                   command=lambda: self.select_font('Calibri'))
        self.font_menu.add_command(label='Courier New',
                                   command=lambda: self.select_font('Courier'))
        self.font_menu.add_command(label='Garamond',
                                   command=lambda: self.select_font('Garamond'))
        self.font_menu.add_command(label='Georgia',
                                   command=lambda: self.select_font('Georgia'))
        self.font_menu.add_command(label='Helvetica',
                                   command=lambda: self.select_font('Helvetica'))
        self.font_menu.add_command(label='monospace (Recomend Programming)',
                                   command=lambda: self.select_font('monospace'))
        self.font_menu.add_command(label='Serif',
                                   command=lambda: self.select_font('Serif'))
        self.font_menu.add_command(label='Verdana',
                                   command=lambda: self.select_font('Verdana'))
        self.font_menu.add_command(label='Tahoma',
                                   command=lambda: self.select_font('Tahoma'))  # english submenu ends
        self.font_menu.add_command(label='SolaimanLipi (বাংলা)')
        self.font_menu.add_command(label='Nikosh (বাংলা)')
        self.font_menu.add_command(label='Siyamrupali (বাংলা)')
        self.font_menu.add_command(label='Vrinda Lohit Bengali (বাংলা)')
        self.font_menu.add_command(label='Mukti Narrow (বাংলা)')
        self.font_menu.add_command(
            label='Kalpurush (বাংলা)')  # font submenu ends

        self.m3.add_cascade(label='Font', menu=self.font_menu)

        self.font_size = Menu(self.m3, tearoff=0)  # font size menu
        self.m3.add_cascade(label='Size', menu=self.font_size)
        self.font_size.add_command(label='8', command=lambda: self.f_size(8))
        self.font_size.add_command(label='9', command=lambda: self.f_size(9))
        self.font_size.add_command(label='10', command=lambda: self.f_size(10))
        self.font_size.add_command(label='11', command=lambda: self.f_size(11))
        self.font_size.add_command(label='12', command=lambda: self.f_size(12))
        self.font_size.add_command(label='14', command=lambda: self.f_size(14))
        self.font_size.add_command(label='15', command=lambda: self.f_size(15))
        self.font_size.add_command(label='16', command=lambda: self.f_size(16))
        self.font_size.add_command(label='18', command=lambda: self.f_size(18))
        self.font_size.add_command(label='20', command=lambda: self.f_size(20))
        self.font_size.add_command(label='22', command=lambda: self.f_size(22))
        self.font_size.add_command(label='25', command=lambda: self.f_size(25))
        self.font_size.add_command(label='27', command=lambda: self.f_size(27))
        self.font_size.add_command(label='30', command=lambda: self.f_size(30))
        self.font_size.add_command(label='35', command=lambda: self.f_size(35))
        self.font_size.add_command(label='40', command=lambda: self.f_size(40))
        self.font_size.add_command(label='46', command=lambda: self.f_size(46))
        self.font_size.add_command(label='50', command=lambda: self.f_size(50))
        self.font_size.add_command(
            label='60', command=lambda: self.f_size(60))  # size menu ends

        self.m3.add_separator()
        self.m3.add_command(label='Bold', command=self.bold)
        self.m3.add_command(label='Italic', command=self.italic)
        self.m3.add_command(label='Underline', command=self.underline)
        self.m3.add_separator()
        self.m3.add_command(label='Close', command=quit)

        # the third menu is ended.
        self.main_menu.add_cascade(label='Selection', menu=self.m3)

        # menu 4
        # this is the vertical menubar
        self.m4 = Menu(self.main_menu, tearoff=0)
        self.m4.add_command(label='Welcome', command=self.welcome)
        self.m4.add_command(label='Documentation', command=self.doc)
        self.m4.add_separator()
        self.m4.add_command(label='Tutorial', command=self.tutorial)
        self.m4.add_command(label='Source Code', command=self.source)
        self.m4.add_command(label='GitHub', command=self.github)
        self.m4.add_separator()
        self.m4.add_command(label='Report Issue', command=self.report)
        self.m4.add_separator()
        self.m4.add_command(label='Check For Updates...', command=self.update)
        self.m4.add_separator()
        self.m4.add_command(label='About', command=self.about)

        self.main_menu.add_cascade(label='Help', menu=self.m4)

        master.config(menu=self.main_menu)

    def select_font(self, font):
        self.text_area.configure(font=font)

    def f_size(self, font_size):
        font_tuple = font.Font(font=self.text_area['font'])
        font_tuple.configure(size=font_size)
        self.text_area.configure(font=font_tuple)

    def bold(self):
        self.text_area.config(font='Arial 14 bold')

    def italic(self):
        self.text_area.config(font='Arial 14 italic')

    def underline(self):
        self.text_area.config(font='Arial 14 underline')

    def welcome(self):
        messagebox.showinfo(
            'Welcome message', 'Welcome to this simple text editor!\nif you like this, please give feedback to us.')

    def doc(self):
        messagebox.askokcancel(
            'Documentation', 'We haven\'t any documentation at this time!')

    def tutorial(self):
        messagebox.askquestion(
            'Tutorial', 'Please follow me to get tutorial!\nlink: https://github.com/mdshakib007')

    def source(self):
        messagebox.askyesno(
            'Source code', 'Source code: https://github.com/mdshakib007/Tkinter-Projects/blob/master/texteditor.py')

    def github(self):
        messagebox.showinfo('Github', 'Github: https://github.com/mdshakib007')

    def report(self):
        messagebox.showerror(
            'Report an issue', 'What\'s gone wrong! please tell us.\nEmail us: shakibahmed00777@gmail.com')

    def update(self):
        messagebox.showwarning(
            'Update', 'Nothing to update!\nYou are using the latest version of NotePaaD')

    def about(self):
        messagebox.showinfo(
            'About', 'This is a simple and opensource notepad, made with python(tkinter), ')

    def new_text_file(self):
        self.text_area.delete(1.0, END)
        self.master.title('Untitled-1   -   NotePaaD')

    def new_file(self):
        self.text_area.delete(1.0, END)
        self.master.title('Untitled-1   -   NotePaaD')

    def open_file(self):
        self.file = filedialog.askopenfilename(
            defaultextension='.txt',
            filetypes=[
                ('All Files', '*.*'), ('Text document',
                                       '*.txt'), ('Python File', '*.py')
            ]
        )

        if self.file == '':
            self.file = None
        else:
            self.master.title(os.path.basename(self.file) + '   -   NotePaaD')
            self.text_area.delete(1.0, END)

            # try to open a file and insert a-z element to the text_area and close the file
            f = open(self.file, 'r')
            self.text_area.insert(1.0, f.read())
            f.close()

    def recent(self):
        self.file = filedialog.askopenfilename(
            defaultextension='.txt',
            filetypes=[
                ('All Files', '*.*'), ('Text Document',
                                       '*.txt'), ('Python File', '*.py')
            ]
        )

        if self.file == '':
            self.file = None
        else:
            self.master.title(os.path.basename(self.file) + '   -   NotePaaD')
            self.text_area.delete(1.0, END)

            f = open(self.file, 'r')
            self.text_area.insert(1.0, f.read())
            f.close()

    def save(self):
        if self.file == None:
            self.file = filedialog.asksaveasfilename(
                initialfile='Untitled.txt',
                defaultextension='.txt',
                filetypes=[
                    ('All Files', '*.*'), ('Text Document',
                                           '*txt'), ('Python File', '*.py')
                ]
            )

            if self.file == '':
                self.file = None
            else:
                f = open(self.file, 'w')
                f.write(self.text_area.get(1.0, END))
                f.close()

                self.master.title(os.path.basename(
                    self.file) + '   -   NotePaaD')
        else:
            f = open(self.file, 'w')
            f.write(self.text_area.get(1.0, END))
            f.close()
            messagebox.showinfo('Save', 'Saved Change')

    def save_as(self):
        if self.file == None:
            self.file = filedialog.asksaveasfilename(
                initialfile='Untitled.txt',
                defaultextension='.txt',
                filetypes=[
                    ('All Files', '*.*'), ('Text Document',
                                           '*.txt'), ('Python File', '*.py')
                ]
            )

            if self.file == '':
                self.file = None
            else:
                f = open(self.file, 'w')
                f.write(self.text_area.get(1.0, END))
                f.close()

                self.master.title(os.path.basename(
                    self.file) + '   -   NotePaaD')

        else:
            self.file = filedialog.asksaveasfilename(
                initialfile='Untitled-1.txt',
                defaultextension='.txt',
                filetypes=[('All Files', '*.*'), ('Text Document',
                                                  '*.txt'), ('Python File', '*.py')
                           ]
            )

            f = open(self.file, 'w')
            f.write(self.text_area.get(1.0, END))
            f.close()

            self.master.title(os.path.basename(self.file) + '   -   NotePaaD')

    def save_all(self):
        messagebox.showerror('File Not Found', 'Multiple file is not found.')

    def share(self):
        messagebox.askokcancel(
            'Share', 'Share to other and modify more.\nSource code: https://github.com/mdshakib007/Tkinter-Projects/blob/master/texteditor.py')

    def undo(self):
        try:
            self.text_area.edit_undo()
        except:
            messagebox.showerror('Error', 'Nothing to undo')

    def redo(self):
        try:
            self.text_area.edit_redo()
        except:
            messagebox.showerror('Error', 'Nothing to redo')

    def cut(self):
        self.text_area.event_generate('<<Cut>>')

    def copy(self):
        self.text_area.event_generate('<<Copy>>')

    def paste(self):
        self.text_area.event_generate('<<Paste>>')

    def resize(self):
        self.master.geometry('888x555')

    def expand(self):
        self.master.geometry('1400x700')

    def change_bg(self):
        colorr = colorchooser.askcolor()
        self.text_area.config(bg=colorr[1])

    def font_color(self):
        colorr = colorchooser.askcolor()
        self.text_area.config(fg=colorr[1])


if __name__ == '__main__':
    root = Tk()
    NotePaaD(root)
    root.mainloop()
