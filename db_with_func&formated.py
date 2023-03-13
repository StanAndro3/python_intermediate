import tkinter
from tkinter import messagebox
from tkinter import *
import mysql.connector
import numpy as np


global name,age
root = Tk()

def Find():
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="newdb")
    cur = con.cursor()
    nm = name.get()
    n = age.get()
    query = "select * from data where name='{0}' and age='{1}'".format(nm, n)
    
    cur.execute(query)
    rows = cur.fetchall()
    con.commit()
    con.close()
    
    messagebox.showinfo(message="done"+"\n"+ str(rows))
    #messagebox.showinfo(message="hello  {0}  youre  {1}  years old".format(nm,n) )

def GetAll():
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="newdb")
    cur = con.cursor()
    nm = name.get()
    n = age.get()
    query = "select * from data"
    
    cur.execute(query)
    rows = cur.fetchall()
    rowscon = np.array(rows)
    con.commit()
    con.close()
    
    messagebox.showinfo(message="all data" +"\n" + str((rowscon)))
    #messagebox.showinfo(message="hello  {0}  youre  {1}  years old".format(nm,n) )

def clicked():
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="newdb")
    cur = con.cursor()
    nm = name.get()
    n = age.get()
    query = "INSERT INTO data VALUES('{0}','{1}')".format(nm,n)
    
    cur.execute(query)
    con.commit()
    con.close()
    
    messagebox.showinfo("done")
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
Button(root,width="7",text="try",command=clicked).place(x=100,y=200)
Button(root,width="17",text="FIND RECORD",command=Find).place(x=100,y=250)
Button(root,width="17",text="GET ALL RECORDS",command=GetAll).place(x=100,y=300)


root.mainloop()