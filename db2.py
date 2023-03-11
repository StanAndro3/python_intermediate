
import mysql
import mysql.connector



con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="testdb")
if con:
    print("connected")
    
else: print("no connection made")
def View():
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="testdb")
    cur = con.cursor()
    query = "SELECT * FROM details"
    cur.execute(query)
    rows = cur.fetchall()
    con.close()
    #print("before............................")
    print(rows)


def Insert():
    con = mysql.connector.Connect(host="localhost", 
                              port=3306, user="root",
                                password="",
                                db="testdb")
    cur = con.cursor()
    query = "INSERT INTO details values  ('faaamaroxx','899','cdc@mail.com','nfgbf') "
    cur.execute(query)
    con.commit()
    con.close()
    print("after.............................")
    View()


Insert()

