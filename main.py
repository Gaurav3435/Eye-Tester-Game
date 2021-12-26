import json 
from tkinter import *
from function import donothing,menu_bar,main_title,display_main_color,create_option_color,return_rgb,create_frame,create_application_button,show_score
def main():
    root =Tk()
    root.title("Eye Test")
    root.geometry("900x650")
    root.maxsize(900, 700)
    root.minsize(900, 600)
    root=menu_bar(root)
    root=main_title(root,30,"Roman")
    rgb=return_rgb()
    root=display_main_color(root,rgb[0],rgb[1],rgb[2])
    root=create_application_button(root)
    root=create_frame(root)
    root=create_option_color(root,rgb[0],rgb[1],rgb[2])
    root.mainloop() 
main()