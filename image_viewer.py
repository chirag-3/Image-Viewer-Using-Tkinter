from tkinter import *
from PIL import ImageTk,Image

root = Tk()

label = Label(root,text="hello",width=50,height=10)
label.grid(row=0,column=0,columnspan=5,rowspan=10,sticky="nsew")

back_button = Button(root,text="back")
back_button.grid(row=10,column=0,sticky="nsew")

next_button = Button(root,text="next")
next_button.grid(row=10,column=4,sticky="nsew")


pictutes = []




root.mainloop()