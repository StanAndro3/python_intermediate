import os
import numpy as np
import threading


def main():
    in1 = str(input("enter any string:")).split(" ")
    np.array(in1)
    filename = "input.txt"
    x = os.path.exists(filename)
    if x:
        path = os.getcwd()
        opener = open(filename,"r")
        reader = opener.readlines()
       
        print("reading from input file " + filename + "at" +" "+path)
        #check if the contents are similar
        for line in reader:
            if str(line)==str(in1):
                print("same lines exist in file " + str(filename) + " at " +str(line[0:]))
            elif str(line) != str(in1):
                opener = open(filename,"w")
                
                opener.close()
                opener = open(filename,"r")
                reader = opener.readlines()
                
                
            
        opener.close()        
        print(reader)
    elif not x:
        path = os.getcwd() + filename
        opener = open(filename,"w")
        writer = opener.writelines(in1)
        opener.close()
        print("written to file......" + " " + filename)
        #read now the contents
        print("reading from file......" + " " + filename + "..." +path)
        openerReader = open(filename,"r")
        contents = openerReader.readlines()
        openerReader.close()
        print(contents)

main()
