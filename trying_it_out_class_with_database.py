import tkinter
from tkinter import messagebox
from tkinter import *
import mysql
import mysql.connector

global name,age
root = Tk()

class Main:
    def clicked():
        con = mysql.connector.connect(host="localhost",
                                      port="3306",user="root",
                                      password="",db="newdb")
        nm = name.get()
        n = age.get()
        query = "INSERT INTO data(name,age) VALUES ({0},{1})".format(nm,n)
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo(message="Success")
        #messagebox.showinfo(message="hello  {0}  youre  {1}  years old".format(nm,n) )

age = IntVar()
name = StringVar()
root.geometry = "400*800"
root.title="hello"
root['bg'] = "grey"

Label(root,width="19",text="name").place(x=20,y=10)
Entry(root,width="19",textvariable=name).place(x=20,y=60)
Label(root,width="19",text="age").place(x=20,y=110)
Entry(root,width="19",textvariable=age).place(x=20,y=160)
Button(root,width="7",text="try",command=Main.clicked).place(x=100,y=200)


root.mainloop()