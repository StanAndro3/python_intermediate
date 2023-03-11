import os
import sys
import sysconfig
import pathlib
import mysql.connector
import mysql
import numpy as np

def main():
    con = mysql.connector.connect(host="localhost", port="3306",
                                  user="root", password="",
                                  db="testdb")
    cur = con.cursor()
    query ="select * from tb"
    cur.execute(query)
    rows= cur.fetchall()
    cur.close()
    #print(rows)
    #creating.............
    mf = np.array(rows)
    #check if file exists
    #if not then create new file
    filename = "myfile.txt"
    x = os.path.exists(filename)
    #if x is false create the file
    if x is True:
        path = os.getcwd() #get current working directory
        #path2 = os.get_exec_path() #get excecution path
        print("file could not be created because it already exists at " + path)
        print("reading from the file..........." + filename)
        initread = open(filename,"r")
        x = initread.readlines()
        #close the file for reading
        print("reading file contents..." + "\n" +str(x))
        initread.close()

       
    elif x is False:
        file = open(filename,"w")
        lsconv = str(rows)
        file.write(lsconv)
        file.close()
        if file:
            print("file created")
        else: print("file not created")
        
main()
