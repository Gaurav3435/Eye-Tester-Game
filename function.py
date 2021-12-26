from tkinter import *
import random
import os,sys
import json


def show_score(root):
    out_file = open("score.json", "r") 
    json_score=json.load(out_file)
    out_file.close()
    score_label = Label(root, text = 'Your Score is: {}'.format(json_score['score']),font=("Arial", 20))
    score_label.pack(pady=5)
    return root


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def quit_game(root):
    out_file = open("score.json", "r") 
    json_score=json.load(out_file)
    out_file.close()
    json_score['score']= 0
    out_file = open("score.json", "w") 
    json.dump(json_score, out_file)
    out_file.close()
    root.destroy()

def create_application_button(root):
    quit_ = Button(root, text = 'Quit', width=20 ,command =lambda: quit_game(root))
    quit_.pack(side=BOTTOM,pady=10)
    change = Button(root, text = 'change', width=20,command =restart_program)
    change.pack(side=BOTTOM,pady=10)
    return root

def create_frame(root):
    frame = Frame(root, relief=RAISED, borderwidth=1)
    frame.pack(fill=BOTH, expand=True)
    frame=show_score(frame)
    return root

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb 

def return_rgb():
    r=random.randint(0,255)
    g=random.randint(0,0)
    b=random.randint(0,255)
    return (r,g,b)

def get_answer(text_label):
    global diff_bar,score

    if text_label==diff_bar.index(min(diff_bar))+1:
        out_file = open("score.json", "r") 
        json_score=json.load(out_file)
        out_file.close()
        json_score['score']= json_score['score']+1
        out_file = open("score.json", "w") 
        json.dump(json_score, out_file)
        out_file.close()
        print("True",json_score['score'])
        restart_program()
    else:
        out_file = open("score.json", "r") 
        json_score=json.load(out_file)
        out_file.close()
        json_score['score']= json_score['score']-1
        out_file = open("score.json", "w") 
        json.dump(json_score, out_file)
        out_file.close()
        print("False",json_score['score'])
        restart_program()


def get_text_over_button(text_label):
    get_answer(text_label)
    

def create_option_color(root,r=0,g=0,b=0):
    global diff_bar
    diff_bar=[]
    text_label=0

    diff_bar.append(random.randint(0,255))
    text_label=text_label+1
    c1=text_label
    color_1= Button (root,text='{}'.format(text_label), bg=from_rgb((r,g+diff_bar[text_label-1],b)),width=10,height=5,command =lambda:get_text_over_button(c1))
    color_1.pack(side=LEFT,pady=50,padx=10,anchor=CENTER)

    diff_bar.append(random.randint(0,255))
    text_label=text_label+1
    c2=text_label
    color_2= Button (root,text='{}'.format(text_label), bg=from_rgb((r,g+diff_bar[text_label-1],b)),width=10,height=5,command =lambda:get_text_over_button(c2))
    color_2.pack(side=LEFT,pady=50,padx=10,anchor=CENTER)

    diff_bar.append(random.randint(0,255))
    text_label=text_label+1
    c3=text_label
    color_3= Button (root,text='{}'.format(text_label), bg=from_rgb((r,g+diff_bar[text_label-1],b)),width=10,height=5,command =lambda:get_text_over_button(c3))
    color_3.pack(side=LEFT,pady=50,padx=10,anchor=CENTER)

    diff_bar.append(random.randint(0,255))
    text_label=text_label+1
    c4=text_label
    color_4= Button (root,text='{}'.format(text_label), bg=from_rgb((r,g+diff_bar[text_label-1],b)),width=10,height=5,command =lambda:get_text_over_button(c4))
    color_4.pack(side=LEFT,pady=50,padx=10,anchor=CENTER)

    diff_bar.append(random.randint(0,255))
    text_label=text_label+1
    c5=text_label
    color_5= Button (root,text='{}'.format(text_label), bg=from_rgb((r,g+diff_bar[text_label-1],b)),width=10,height=5,command =lambda:get_text_over_button(c5))
    color_5.pack(side=LEFT,pady=50,padx=10,anchor=CENTER)

    diff_bar.append(random.randint(0,255))
    text_label=text_label+1
    c6=text_label
    color_6= Button (root,text='{}'.format(text_label), bg=from_rgb((r,g+diff_bar[text_label-1],b)),width=10,height=5,command =lambda:get_text_over_button(c6))
    color_6.pack(side=LEFT,pady=50,padx=10,anchor=CENTER)

    diff_bar.append(random.randint(0,255))
    text_label=text_label+1
    c7=text_label
    color_7= Button (root,text='{}'.format(text_label), bg=from_rgb((r,g+diff_bar[text_label-1],b)),width=10,height=5,command =lambda:get_text_over_button(c7))
    color_7.pack(side=LEFT,pady=50,padx=10,anchor=CENTER)

    diff_bar.append(random.randint(0,255))
    text_label=text_label+1
    c8=text_label
    color_8= Button (root,text='{}'.format(text_label), bg=from_rgb((r,g+diff_bar[text_label-1],b)),width=10,height=5,command =lambda:get_text_over_button(c8))
    color_8.pack(side=LEFT,pady=50,padx=10,anchor=CENTER)

    diff_bar.append(random.randint(0,255))
    text_label=text_label+1
    c9=text_label
    color_9= Button (root,text='{}'.format(text_label), bg=from_rgb((r,g+diff_bar[text_label-1],b)),width=10,height=5,command =lambda:get_text_over_button(c9))
    color_9.pack(side=LEFT,pady=50,padx=10,anchor=CENTER)

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

def main_title(root,size=20,type_="Arial"):
    main_title = Label(root, text = 'Eye Tester',font=(type_, size))
    main_title.pack(side=TOP,pady=40)
    return root