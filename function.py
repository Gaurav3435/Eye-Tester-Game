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

def restart_game(root):
    out_file = open("score.json", "r") 
    json_score=json.load(out_file)
    out_file.close()
    json_score['score']= 0
    out_file = open("score.json", "w") 
    json.dump(json_score, out_file)
    out_file.close()
    restart_program()


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
    canvas.pack(side=TOP,pady=5)
    return root

def donothing(root):
    button = Button(root, text="Do nothing button")
    button.pack(side=BOTTOM)

def help_window(root):
    top= Toplevel(root)
    top.geometry("750x250")
    top.title("How to play the Game?")
    Label(top,text= "🤦", font=('Arial 40 bold')).pack(side=TOP)
    Label(top,text= "This is a Simple Game to check your eyes sharpness. ", font=('Arial 10 bold')).pack(side=TOP)
    Label(top,text= "You need to select the closest possible shade of the shown color. ", font=('Arial 10 bold')).pack(side=TOP)
    Label(top,text= "The more accurate you are is choosing the closest posssible shade the more you score.", font=('Arial 10 bold')).pack(side=TOP)
    Label(top,text= "Each accuracte prediction add 1 point to score.The Wrong prediction would lead to reduction of score by 1 point.", font=('Arial 10 bold')).pack(side=TOP)
    Label(top,text= "Let's check how much sharp your eyes are?", font=('Arial 10 bold')).pack(side=TOP)
    Label(top,text= "😉", font=('Arial 40 bold')).pack(side=TOP)

def about_window(root):
    top= Toplevel(root)
    top.geometry("750x250")
    top.title("About the Application?")
    Label(top,text= "This application is build using Python programming langauge. 😎", font=('Arial 15 bold')).pack(side=TOP)
    Label(top,text= "THe GUI is build using Tkinter Library!❤", font=('Arial 15 bold')).pack(side=TOP)
    Label(top,text= "This is open Source Project, wanted to contribute ?", font=('Arial 15 bold')).pack(side=TOP)
    Label(top,text= "🐱‍👤", font=('Arial 25 bold')).pack(side=TOP)
    Label(top,text= "Checkout this github link below!", font=('Arial 15 bold')).pack(side=TOP)
    Label(top,text= "🐱‍🏍", font=('Arial 25 bold')).pack(side=TOP)
    Label(top,text= "https://github.com/Gaurav3435/Eye-Tester-Game", font=('Arial 15 bold')).pack(side=TOP)


def developer_window(root):
    top= Toplevel(root)
    top.geometry("750x300")
    top.title("About the Developer?")
    Label(top,text= "Ahh now you are at a right place", font=('Arial 15 bold')).pack(side=TOP)
    Label(top,text= "😜", font=('Arial 15 bold')).pack(side=TOP)
    Label(top,text= "Hiiiii , My Name is Gaurav Patil !!!", font=('Arial 15 bold')).pack(side=TOP)
    Label(top,text= "Hope you have liked my project", font=('Arial 15 bold')).pack(side=TOP)
    Label(top,text= "🤞", font=('Arial 25 bold')).pack(side=TOP)
    Label(top,text= "Wanted to contact? You can email me 😁", font=('Arial 15 bold')).pack(side=TOP)
    Label(top,text= "🤔", font=('Arial 25 bold')).pack(side=TOP)
    Label(top,text= "gauravpatil2232001@gmail.com", font=('Arial 15 bold')).pack(side=TOP)

def menu_bar(root):
    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Game", command=lambda:restart_game(root))
    filemenu.add_command(label="Change Color", command=restart_program)
    filemenu.add_command(label="Reset Score", command=lambda:restart_game(root))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Menu", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help", command=lambda: help_window(root))
    helpmenu.add_command(label="About...", command=lambda: about_window(root))
    helpmenu.add_command(label="Developer", command=lambda: developer_window(root))
    filemenu.add_separator()
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    return root

def main_title(root,size=20,type_="Arial"):
    main_title = Label(root, text = ' Eye Tester ',font=(type_, size))
    main_title.pack(side=TOP,pady=20)
    Label(root, text = '👀',font=(12)).pack(side=TOP,pady=5)
    return root