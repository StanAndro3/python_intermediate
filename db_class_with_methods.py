
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import tkinter

from tkinter import messagebox
from tkinter import *
import mysql
import mysql.connector

global name,age
root = Tk()

class Main:
    def clicked(self,name,age):
        ##
        #nm = name
        self.name = name
        nm = getattr(self,name)
        #n = age.get()
        self.age = age
        n= getattr(self,age)
        messagebox.showinfo(message="hello  {0}  youre  {1}  years old".join(self,nm,n) )

age = IntVar()
name = StringVar()
root.geometry = "400*800"
root.title="hello"
root['bg'] = "grey"

Label(root,width="19",text="name").place(x=20,y=10)
Entry(root,width="19",textvariable=name).place(x=20,y=60)
Label(root,width="19",text="age").place(x=20,y=110)
Entry(root,width="19",textvariable=age).place(x=20,y=160)
Button(root,width="7",text="try",command=Main()).place(x=100,y=200)


root.mainloop()