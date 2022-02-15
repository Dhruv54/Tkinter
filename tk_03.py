from tkinter import *

root=Tk()

root.title("Compression Decompression")
height=700
width=400
root.geometry(f"{height}x{width}")

# Frame in Tkinter

frame=Frame(root,bg="black",borderwidth=5,relief=RIDGE)
frame.pack(side=LEFT,fill=Y)

label=Label(frame,text="Welcome Back Dhruv!!!",foreground="white",bg="black")
label.pack(pady=5)

frame1=Frame(root,bg="skyblue",borderwidth=5,relief=GROOVE)
frame1.pack(side=TOP,fill=X)

label1=Label(frame1,text="Compression Decompression",foreground="black",bg="skyblue")
label1.pack(pady=5)

root.mainloop()