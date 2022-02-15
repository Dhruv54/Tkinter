from tkinter import *
from tkinter import font

root=Tk()

root.title("Compression Decompression")
height=700
width=400
root.geometry(f"{height}x{width}")

#   Define function for button
def compress():
    print("Compression Done!!!")
# Button in Tkinter
f1=Frame(root,bg="grey")
f1.pack(side=TOP,fill=X)
button =Button(f1,text="Compress",font="comicsans 10 bold",command=compress)
button.pack(pady=10)

root.mainloop()