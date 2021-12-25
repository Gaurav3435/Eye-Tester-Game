from tkinter import *
import random
import os,sys

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def create_application_button(root):
    quit_ = Button(root, text = 'Quit', width=20 ,command = root.destroy)
    quit_.pack(side=BOTTOM,pady=10)
    change = Button(root, text = 'change', width=20,command =restart_program)
    change.pack(side=BOTTOM,pady=10)
    return root

def create_frame(root):
    frame = Frame(root, relief=RAISED, borderwidth=1)
    frame.pack(fill=BOTH, expand=True)
    return root

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb 

def return_rgb():
    r=random.randint(0,255)
    g=random.randint(0,0)
    b=random.randint(0,255)
    return (r,g,b)

def create_option_color(root,r=0,g=0,b=0):
    diff_bar=[]
    for i in range(9):
        diff_bar.append(random.randint(0,255))
        color_= Button (root, bg=from_rgb((r,g+diff_bar[i],b)),width=10,height=5)
        color_.pack(side=LEFT,pady=50,padx=10,anchor=CENTER)
    print(diff_bar)
    return root

def display_main_color(root,r=0,g=0,b=0):
    canvas = Canvas(root, width = 200, height = 200,bg=from_rgb((r, g, b)))  
    canvas.pack(side=TOP)
    return root

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack(side=BOTTOM)

def menu_bar(root):
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)
    return root

def create_image(root):
    
    return root

def main_title(root,size=20,type_="Arial"):
    main_title = Label(root, text = 'Eye Tester',font=(type_, size))
    main_title.pack(side=TOP,pady=40)
    return root