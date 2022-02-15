from tkinter import *
root=Tk()

root.title("Compression Decompression")
height=700
width=400
root.geometry(f"{height}x{width}")

def getval():
    print(f"{usernamevalue.get()} and {passwordvalue.get()}")
# Grid In Tkinter
username=Label(root,text="UserName")
password=Label(root,text="Password")
username.grid(row=0)
password.grid(row=1)

usernamevalue=StringVar()
passwordvalue=StringVar()
usernameentry=Entry(root,textvariable=usernamevalue)
passwordentry=Entry(root,textvariable=passwordvalue)
usernameentry.grid(row=0,column=1,padx=3,pady=3)
passwordentry.grid(row=1,column=1,padx=3,pady=3)

Button(text="submit",command=getval).grid(row=4,column=1,pady=3)

root.mainloop()