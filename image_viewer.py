from tkinter import *
from PIL import ImageTk,Image

root = Tk()

p1 = ImageTk.PhotoImage(Image.open("G:\E drive\Code\Tkinter\Image_Viewer\photos\\abcd1.jpeg"))

label = Label(root,image = p1)
label.grid(row=0,column=0,columnspan=5,rowspan=10,sticky="nsew")

next_button = None
back_button = None
index = 0

# def go_back(i,l,photos,b):
    
#     img = ImageTk.PhotoImage(Image.open(photos[i-1]))
#     label.configure(image=img)
#     label.image = img

#     if i==0:
#         b['state'] = DISABLED

def go_back(l,photos):
    
    global index
    img = ImageTk.PhotoImage(Image.open(photos[index-1]))
    label.configure(image=img)
    label.image = img
    index = index -1
    if index==0:
        back_button['state'] = DISABLED
    next_button['state'] = NORMAL

# def go_next(i,l,photos,b,bb):
#     img = ImageTk.PhotoImage(Image.open(photos[i+1]))
#     label.configure(image=img)
#     label.image = img

#     if i==l:
#         b['state'] = DISABLED
#     bb['state'] = NORMAL


def go_next(l,photos):
    global index
    img = ImageTk.PhotoImage(Image.open(photos[index+1]))
    label.configure(image=img)
    label.image = img
    index = index + 1
    if index==l:
        next_button['state'] = DISABLED
    back_button['state'] = NORMAL



photos = ["G:\E drive\Code\Tkinter\Image_Viewer\photos\\abcd1.jpeg",
          "G:\E drive\Code\Tkinter\Image_Viewer\photos\\abcd2.jpeg",
          "G:\E drive\Code\Tkinter\Image_Viewer\photos\\abcd3.jpeg",
          "G:\E drive\Code\Tkinter\Image_Viewer\photos\\abcd4.jpeg",
          "G:\E drive\Code\Tkinter\Image_Viewer\photos\\abcd5.jpeg",
          "G:\E drive\Code\Tkinter\Image_Viewer\photos\\abcd6.jpeg",
          "G:\E drive\Code\Tkinter\Image_Viewer\photos\\abcd7.jpeg"]

l = len(photos) - 1

back_button = Button(root,text="back",command = lambda : go_back(l,photos),state = DISABLED)
back_button.grid(row=10,column=0,sticky="nsew")

next_button = Button(root,text="next",command = lambda : go_next(l,photos))
next_button.grid(row=10,column=4,sticky="nsew")
if l == 1:
  next_button['state'] = DISABLED



root.mainloop()