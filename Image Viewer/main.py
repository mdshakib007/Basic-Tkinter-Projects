from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageDraw
import os
from tkinter import messagebox


# gloabl variables
file = None
screen_width = 800
screen_height = 800
scale_factor = 1.0



root = Tk()
root.geometry(f'{screen_width}x{screen_height}')
root.title('Image Viewer')



def open_image():
    global file
    file = askopenfilename(initialdir=os.getcwd(), title='Select An Image',
                           filetypes=(('JPG Image', '*.jpg'),
                                      ('PNG Image', '*.png'),
                                      ('JPEG Image', '*.jpeg'),
                                      ('All Files', '*.*')), 
                           )
    image_name = Image.open(file)
    img = ImageTk.PhotoImage(image=image_name)
    
    # plot image in label
    photo_label.config(image=img)
    photo_label.image=img
    
    
def save_file():
    if file is not None:
        image = Image.open(file)
        image.save(file)
        
        

def save_as():
    global file
    
    if file is not None:
        new_file = asksaveasfilename(initialdir=os.getcwd(), title='Select An Image',
                           filetypes=(('JPG Image', '*.jpg'),
                                      ('PNG Image', '*.png'),
                                      ('JPEG Image', '*.jpeg'),
                                      ('All Files', '*.*')), 
                           )
        
        if new_file:
            new_image = Image.open(new_file)
            new_image.save(new_file)
            
            file = new_file


def best_fit():
    global file
    if file is not None:
        image_file = Image.open(file)
        width, height = root.winfo_width(), root.winfo_height()
        resized = image_file.resize((width, height))
        img = ImageTk.PhotoImage(resized)
        
        # plot resized image
        photo_label.config(image=img)
        photo_label.image = img
        
        
def square_fit():
    global file
    if file is not None:
        image_file = Image.open(file)
        resized = image_file.resize((800, 800))
        img = ImageTk.PhotoImage(image=resized)
        
        # plot
        photo_label.config(image=img)
        photo_label.image = img


def zoom_in():
    global scale_factor
    
    if file is not None and Event.delta > 0:
        scale_factor *= 20
        image = Image.open(file)
        width, height = int(image.width * scale_factor), int(image.height * scale_factor)
        resized_image = image.resize((width, height))
        img = ImageTk.PhotoImage(resized_image)
        
        # plot img
        photo_label.config(image=img)
        photo_label.image = img
    
    

def zoom_out():
    global scale_factor
    if file is not None and Event.delta < 0:
        scale_factor /= 20
        image = Image.open(file)
        width, height = int(image.width * scale_factor), int(image.height * scale_factor)
        
        resized_img = image.resize((width, height))
        img = ImageTk.PhotoImage(image=resized_img)
        
        
        # plot 
        photo_label.config(image=img)
        photo_label.image = img
        
        

def how_works():
    messagebox.showinfo("How It's Work?", "Not Ready Yet!")

def report():
    pass

def source_code():
    pass

def about():
    pass


## Menu
main_menu = Menu(root)

# file menu
file_menu = Menu(main_menu, tearoff=False)

file_menu.add_command(label='Open...', command=open_image)
file_menu.add_command(label='Open Location', command=open_image)
file_menu.add_separator()
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As...', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit)

main_menu.add_cascade(menu=file_menu, label='File', font='Arial 13')

# Edit menu
edit_menu = Menu(main_menu, tearoff=0)

edit_menu.add_command(label='Zoom In', command=zoom_in)
edit_menu.add_command(label='Zoom Out', command=zoom_out)
edit_menu.add_command(label='Crop', command=lambda: messagebox.showerror('Crop', "This Feature Is Not Ready!"))
edit_menu.add_separator()
edit_menu.add_command(label='Best Fit', command=best_fit)
edit_menu.add_command(label='Square Fit', command=square_fit)
edit_menu.add_separator()
edit_menu.add_command(label='Quit', command=exit)

main_menu.add_cascade(menu=edit_menu, label='Edit', font='Arial 13')


# help menu
help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label="How It's Work?", command=how_works)
help_menu.add_command(label="Report An Issue...", command=report)
help_menu.add_command(label="Get Source Code", command=source_code)
help_menu.add_separator()
help_menu.add_command(label="About", command=about)

main_menu.add_cascade(menu=help_menu, label='Help', font='Arial 13')

root.config(menu=main_menu)



### label for plot an image
photo_label = Label(root)
photo_label.pack()

## bind mouse wheel
photo_label.bind('<MouseWheel>', zoom_in)
photo_label.bind('<Shift-MouseWheel>', zoom_out)


root.mainloop()