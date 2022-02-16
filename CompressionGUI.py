from tkinter import *

root=Tk()
root.title("Compression-Decompression - Tkinter(Python)")
width=800
height=500
root.geometry(f"{width}x{height}")
root.wm_iconbitmap("compress.ico")
root.config(background="#3AAFA9")
header=Label(root,text="Text-Compression",font="Sans-serif 20 bold",background="#3AAFA9",pady=10,padx=10)
header.pack(side=TOP)

button = Button(root, text="Click me!",width=100,height=100)
img = PhotoImage(file="C:/Users/Dhruv j Patel/Desktop/Tkinter/Tkinter/upload.png") # make sure to add "/" not "\"
button.config(image=img)
button.pack()


root.mainloop()