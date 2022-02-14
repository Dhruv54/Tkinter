from tkinter import *
from PIL import Image,ImageTk

root=Tk()

root.geometry("600x300")    #   (width,height)
root.minsize(400,400)
root.maxsize(1100,600)
label=Label(text="Welcome to Our App")
label.pack()

_img=Image.open('test.jpg')
photo=ImageTk.PhotoImage(_img)
img_label=Label(image=photo)
img_label.pack()
root.mainloop()