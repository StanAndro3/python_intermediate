import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import Menubutton
from tkinter import OptionMenu

root = Tk()

def clicked():
    n = age.get()
    messagebox.showinfo(message="hello " + n)

age = StringVar()
root.geometry = "400*800"
root.title="hello"
root['bg'] = "grey"

Entry(root,width="19",textvariable=age).pack()
Button(root,width="7",text="try",command=clicked).place(x=100,y=200)
Menubutton(root,width="8",text="try").place(x=400,y=600)

root.mainloop()