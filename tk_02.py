from cgitb import text
from textwrap import fill
from tkinter import *
from turtle import width

root=Tk()

root.title("Compression Decompression")
height=700
width=400
root.geometry(f"{height}x{width}")

label=Label(text="Welcome to Our Python Apllication!!",bg="blue",fg="white",font="comicsans 16 bold",borderwidth=10,relief=GROOVE,padx=10,pady=10)
label.pack(side=TOP,fill=X)
label1=Label(text="Compression Copyright@2022",bg="black",fg="white",padx=10,pady=10).pack(side=BOTTOM,fill=X)


root.mainloop()