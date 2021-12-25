from tkinter import *
from function import donothing,menu_bar,main_title,create_image

root =Tk()
root.title("Eye Test")
root.geometry("900x650")
root=menu_bar(root)
root=main_title(root,18,"Roman")
root=create_image(root)
root.mainloop()