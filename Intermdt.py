#this should be the intermediate file for release
#still on trial release

"""=========BEGIN HERE======"""
import tkinter
from tkinter import messagebox
from tkinter import *
import os
import sys
import sysconfig
import pathlib
import numpy as np
import mysql
import mysql.connector
import numpy as np
root = Tk()
root['bg'] = "grey"
root.geometry="500*500"
root.title = "my title"

global car_name, amount_paid,car_year,car_color,fuel_capacity,manufacturer,serial_plate
global no_of_doors, customer_name,customer_id,customer_phone

#instantiate the variables type

car_name = StringVar()
amount_paid = IntVar()
car_year = IntVar()
car_color = StringVar()
fuel_capacity = IntVar()
manufacturer = StringVar()
serial_plate = StringVar()
no_of_doors = IntVar()
customer_name = StringVar()
customer_id = IntVar()
customer_phone = StringVar()
#sql connection
con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="cardb")
if con:
    print("connected")


#what happens when register car button is pressed
def Register():#entering new record into the database
    ##REVISITED
    #get all variables

    cn = car_name.get()
    ap = amount_paid.get()
    cy = car_year.get()
    cc = car_color.get()
    fc = fuel_capacity.get()
    manf = manufacturer.get()
    sp = serial_plate.get()
    ndoors = no_of_doors.get()
    csn = customer_name.get()
    csid = customer_id.get()
    csphone = customer_phone.get()

#####################################
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="cardb")
    cur = con.cursor()
    query = "INSERT INTO details(car_name, amount_paid,car_year,car_color,fuel_capacity,manufacturer,serial_plate,no_of_doors, customer_name,customer_id,customer_phone) VALUES('{0}', '{1}', '{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')".format(cn,ap,cy,cc,fc,manf,sp,ndoors,csn,csid,csphone)
    cur.execute(query)
    con.commit()
    con.close()
    #mf = np.array(rows)
    #check if file exists
    #if not then create new file
    #filename = "myfile.txt"
    #x = os.path.exists(filename)
    #if x is false create the file
    #if x is True:
    #    path = os.getcwd() #get current working directory
    #   #path2 = os.get_exec_path() #get excecution path
    #    print("file could not be created because it already exists at " + path)
    #    print("reading from the file..........." + filename)
    #    initread = open(filename,"r")
    #    x = initread.readlines()
        #close the file for reading
    #    print("reading file contents..." + "\n" +str(x))
    #    initread.close()

       
    #elif x is False:
    #    file = open(filename,"w")
    #    lsconv = str(rows)
    #    file.write(lsconv)
    #    file.close()
    #    if file:
    #        print("file created")
    #    else: print("file not created")
    #print("before............................")
    #print(lsconv)
    messagebox.showinfo(root,message="CAR RECORD MADE SUCCESSFULLY !!!")





def Find():#finding one record only # PLEASE REVISIT THIS !!!
    cn = car_name.get()
    ap = amount_paid.get()
    cy = car_year.get()
    cc = car_color.get()
    fc = fuel_capacity.get()
    manf = manufacturer.get()
    sp = serial_plate.get()
    ndoors = no_of_doors.get()
    csn = customer_name.get()
    csid = customer_id.get()
    csphone = customer_phone.get()
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="cardb")
    cur = con.cursor()
    query = "SELECT * FROM details where car_name='{0}' ,car_price='{1}', car_year='{2}',car_color='{3}' ,fuel_capacity='{4}',manufacturer='{5}',serial_plate='{6}' ,no_of_doors ='{7}',customer_name='{8}',customer_id='{9}',customer_phone='{10}'".format(cn,ap,cy,cc,fc,manf,sp,ndoors,csn,csid,csphone)

    ##REVISITED
    ##REVISITED
    cur.execute(query)
    rows = cur.fetchall()
    con.commit()
    showrows = np.arange((rows))
    con.close()
    #mf = np.array(rows) 
    #check if file exists
    #if not then create new file
    #filename = "myfile.txt"
    #x = os.path.exists(filename)
    #if x is false create the file
    #if x is True:
        #path = os.getcwd() #get current working directory
        #path2 = os.get_exec_path() #get excecution path
        #print("file could not be created because it already exists at " + path)
        #print("reading from the file..........." + filename)
        #initread = open(filename,"r")
        #x = initread.readlines()
        #close the file for reading
        #print("reading file contents..." + "\n" +str(x))
        #initread.close()

       
    #elif x is False:
        #file = open(filename,"w")
        #lsconv = str(rows)
        #file.write(lsconv)
        #file.close()
        #if file:
            #print("file created")
        #else: print("file not created")
    #print("before............................")
    #print(rows)
    messagebox.showinfo(root,message="CAR RECORD FOUND ARE AS FOLLOWS :!!!" + "\n" +str(showrows))


def Display():#Displaying all records
    ##REVISITED
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="cardb")
    cur = con.cursor()
    query = "SELECT * FROM details"
    cur.execute(query)
    rows = cur.fetchall()
    showrows = np.array(rows)
    con.commit()
    con.close()
    #print("before............................")
    #print(rows)
    messagebox.showinfo(root,message="ALL DATA !!!" + "\n" +str(showrows))

#++++++++++=======change this to file handler class method
def Generate():
#     con = mysql.connector.Connect(host="localhost", 
                               # port="3306", user="root",
                               # password="",
                               # db="cardb")
    #cur = con.cursor()
    #query = "SELECT * FROM details"
    #cur.execute(query)
    #rows = cur.fetchall()
    #con.commit()
    #con.close()
    #    messagebox.showinfo("no method exists")  
    messagebox.showinfo("file created")

def UpDate():#update records from the database
    cn = car_name.get()
    ap = amount_paid.get()
    cy = car_year.get()
    cc = car_color.get()
    fc = fuel_capacity.get()
    manf = manufacturer.get()
    sp = serial_plate.get()
    ndoors = no_of_doors.get()
    csn = customer_name.get()
    csid = customer_id.get()
    csphone = customer_phone.get()
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="cardb")
    cur = con.cursor()
    query = "SET "
    cur.execute(query)
    con.commit()
    con.close()
    messagebox.showinfo(root,message="SUCCESSFULLY UPDATED !!!")


def Delt():#delete a record from database
    #REVISITED
    cn = car_name.get()
    ap = amount_paid.get()
    cy = car_year.get()
    cc = car_color.get()
    fc = fuel_capacity.get()
    manf = manufacturer.get()
    sp = serial_plate.get()
    ndoors = no_of_doors.get()
    csn = customer_name.get()
    csid = customer_id.get()
    csphone = customer_phone.get()
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="cardb")
    cur = con.cursor()
    query = "delete from details where car_name='{0}' and customer_name='{1}'".format(cn,csn)#REVISITEDD !!
    x = messagebox.askyesno(message="are you sure you want to delete this customer???")
    if x ==True:
        cur.execute(query)
        #rows = cur.fetchall()
        con.commit()
        con.close()
        messagebox.showinfo(root,message="DELETED SUCCESSFULLY  !!!")
    elif x is not True:
        messagebox.showerror(root,message="DELETE ERROR")
        

#==========================FRONT END================================================================

Label(root,text="WELCOME TO CAR SALES PROGRAM.",font="bold",foreground="yellow",background="black",height="3",width=900).pack()
Label(root,text="CAR NAME",font="bold",foreground="aquamarine",background="purple",height="1").place(x=10,y=110)
Entry(root,text="",width="32",textvariable=car_name).place(x=10,y=150)


Label(root,text="AMOUNT PAID",font="bold",foreground="aquamarine",background="purple",height="1").place(x=420,y=110)
Entry(root,width="32",textvariable=amount_paid,).place(x=420,y=150)

Label(root,text="CUSTOMER NAME",font="bold",foreground="aquamarine",background="purple",height="1").place(x=800,y=110)
Entry(root,text="",width="32",textvariable=customer_name).place(x=800,y=150)

Label(root,text="CAR COLOR",font="bold",foreground="aquamarine",background="purple",height="1").place(x=10,y=220)
Entry(root,text="",width="32",textvariable=car_color).place(x=10,y=250)


Label(root,text="CAR YEAR",font="bold",foreground="aquamarine",background="purple",height="1").place(x=420,y=220)
Entry(root,text="",width="32",textvariable=car_year).place(x=420,y=250)

Label(root,text="CUSTOMER ID",font="bold",foreground="aquamarine",background="purple",height="1").place(x=800,y=220)
Entry(root,text="",width="32",textvariable=customer_id).place(x=800,y=250)


Label(root,text="CAR FUEL CAPACITY",font="bold",foreground="aquamarine",background="purple",height="1").place(x=10,y=330)
Entry(root,text="",width="32",textvariable=fuel_capacity).place(x=10,y=360)


Label(root,text="CAR MANUFACTURER",font="bold",foreground="aquamarine",background="purple",height="1").place(x=420,y=330)
Entry(root,text="",width="32",textvariable=manufacturer).place(x=420,y=360)

Label(root,text="CUSTOMER PHONE NUMBER",font="bold",foreground="aquamarine",background="purple",height="1").place(x=800,y=330)
Entry(root,text="",width="32",textvariable=customer_phone).place(x=800,y=360)

Label(root,text="CAR SERIAL PLATE",font="bold",foreground="aquamarine",background="purple",height="1").place(x=10,y=440)
Entry(root,text="",width="32",textvariable=serial_plate).place(x=10,y=470)


Label(root,text="NUMBER OF DOORS",font="bold",foreground="aquamarine",background="purple",height="1").place(x=420,y=440)
Entry(root,text="",width="32",textvariable=no_of_doors).place(x=420,y=470)


Button(root,text="REGISTER CAR",font="bold",foreground="black",background="BLUE",command=Register).place(x=10,y=550)

Button(root,text="FIND RECORD",font="bold",foreground="black",background="green",command=Find).place(x=10,y=600)

Button(root,text="DISPLAY RECORD",font="bold",foreground="black",background="green",command=Display).place(x=200,y=550)

Button(root,text="GENERATE SCRIPT",font="bold",foreground="black",background="yellow",command=Generate).place(x=220,y=600)

Button(root,text="UPDATE RECORD",font="bold",foreground="black",background="orange",command=UpDate).place(x=450,y=550)

Button(root,text="DELETE RECORD",font="bold",foreground="black",background="red",command=Delt).place(x=450,y=600)

Entry(root,background="black",width="900",disabledbackground="black").pack()

#Label(root,background="black",foreground="black",width="1",height="40").place(x=670,y=70)

#Entry(root,background="black",width="900",disabledbackground="black").place(x=0,y=670)


root.mainloop()