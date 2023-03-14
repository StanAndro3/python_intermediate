import mysql
import mysql.connector
import tkinter
from tkinter import *
from tkinter import messagebox
global name

def Insert():
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="testdb")
    #query = "INSERT INTO tb values"
    cur = con.cursor()
    #cur.execute(query)
    #con.commit()
    con.close()
def Show():
    n = name.get()
    messagebox.showinfo(message="hello"+ n)
    


name = StringVar()
master = Tk()
master.geometry ="1600*1600"
master['bg'] = "grey"

#PanedWindow(master,background="blue",height="700",width="700").pack()
#PanedWindow.add(master,Button()

Label(master,text="sales").pack()

Label(master,text="name").place(x=100,y=100)
Entry(master,text="",textvariable=name,width='19',borderwidth="6",).place(x=100,y=150)

Button(master,text="ENTER",width='10',command=Show).place(x=100,y=300)



master.mainloop()