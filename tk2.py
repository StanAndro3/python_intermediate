import tkinter
from tkinter import *
from tkinter import messagebox
import os
import sysconfig
import pathlib
import numpy as np
from numpy import *
from cryptography import *
import matplotlib.pyplot as plt
import sys
import sqlite3
from sqlite3 import *
root = Tk()
root['bg'] = "purple"
root.geometry="500*500"
root.title = "my title"

global car_name, car_price,car_year,car_color,fuel_capacity,manufacturer,serial_plate
global no_of_doors

"""BACK END 001 """#============BACK START    handlers  0=================

def Register():
   
    messagebox.showinfo(root,message="CAR REGISTERED SUCCESSFULLY !!!")


def Find():
    messagebox.showinfo(root,message="CAR RECORD FOUND ARE AS FOLLOWS :!!!")


def Display():
    messagebox.showinfo(root,message="ALL DATA !!!")


def GetR():
    messagebox.showinfo(root,message="YOUR REQUEST WAS  !!!")


def UpDate():
    messagebox.showinfo(root,message="SUCCESSFULLY UPDATED !!!")


def Delt():
    messagebox.showinfo(root,message="DELETED SUCCESSFULLY  !!!")



class users:
    def __init__(self,customer,seller) -> None:
        users.user1 = customer
        users.user2 = seller
    class customer:
        def __init__(self,name,region,phone,car_bought)->None:
            self.name = name
            self.region = region
            self.phone = phone
            self.car_bought = car_bought
    class seller:
        def __init__(self,name,region,phone,car_selling,price) -> None:
            self.name= name
            self.region = region
            self.phone = phone
            self.car_selling = car_selling
            self.price = price
            

#==========================FRONT END================================================================

Label(root,text="WELCOME TO CAR SALES PROGRAM.",font="bold",foreground="yellow",background="black",height="3",width=900).pack()
Label(root,text="CAR NAME",font="bold",foreground="aquamarine",background="purple",height="1").place(x=10,y=110)
Entry(root,text="",width="32").place(x=10,y=150)


Label(root,text="CAR PRICE",font="bold",foreground="aquamarine",background="purple",height="1").place(x=420,y=110)
Entry(root,text="",width="32",textvariable="car_price").place(x=420,y=150)


Label(root,text="CAR COLOR",font="bold",foreground="aquamarine",background="purple",height="1").place(x=10,y=220)
Entry(root,text="",width="32",textvariable="car_color").place(x=10,y=250)


Label(root,text="CAR YEAR",font="bold",foreground="aquamarine",background="purple",height="1").place(x=420,y=220)
Entry(root,text="",width="32",textvariable="car_year").place(x=420,y=250)


Label(root,text="CAR FUEL CAPACITY",font="bold",foreground="aquamarine",background="purple",height="1").place(x=10,y=330)
Entry(root,text="",width="32",textvariable="fuel_capacity").place(x=10,y=360)


Label(root,text="CAR MANUFACTURER",font="bold",foreground="aquamarine",background="purple",height="1").place(x=420,y=330)
Entry(root,text="",width="32",textvariable="manufacturer").place(x=420,y=360)


Label(root,text="CAR SERIAL PLATE",font="bold",foreground="aquamarine",background="purple",height="1").place(x=10,y=440)
Entry(root,text="",width="32",textvariable="serial_plate").place(x=10,y=470)


Label(root,text="NUMBER OF DOORS",font="bold",foreground="aquamarine",background="purple",height="1").place(x=420,y=440)
Entry(root,text="",width="32",textvariable="no_of_doors").place(x=420,y=470)


Button(root,text="REGISTER CAR",font="bold",foreground="black",background="BLUE",command=Register).place(x=10,y=550)

Button(root,text="FIND RECORD",font="bold",foreground="black",background="green",command=Find).place(x=10,y=600)

Button(root,text="DISPLAY RECORD",font="bold",foreground="black",background="green",command=Display).place(x=200,y=550)

Button(root,text="GET RECORD",font="bold",foreground="black",background="yellow",command=GetR).place(x=220,y=600)

Button(root,text="UPDATE RECORD",font="bold",foreground="black",background="orange",command=UpDate).place(x=450,y=550)

Button(root,text="DELETE RECORD",font="bold",foreground="black",background="red",command=Delt).place(x=450,y=600)

Entry(root,background="black",width="900",disabledbackground="black").pack()

Label(root,background="black",foreground="black",width="1",height="40").place(x=670,y=70)

Entry(root,background="black",width="900",disabledbackground="black").place(x=0,y=670)









#==========================================BACK END 002   ============================================

















root.mainloop()