import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql

windo = tkinter.Tk()

windo.geometry("800x450")

L = Label(windo, text="Enter Student ID:", font=('arial',30),fg='blue')
L.grid(row=0, column=0)
E = Entry(windo,bd=5,width=50)
E.grid(row=0, column= 1)

L1 = Label(windo, text="Enter Student Name:", font=('arial',30),fg='blue')
L1.grid(row=1, column=0)
E1 = Entry(windo,bd=5,width=50)
E1.grid(row=1, column= 1)

L2 = Label(windo, text="Enter Student Address:", font=('arial',30),fg='blue')
L2.grid(row=2, column=0)
E2 = Entry(windo,bd=5,width=50)
E2.grid(row=2, column= 1)


def myButtonEvent(selection):
    print("Student Id: ", E.get())
    print("Student Name: ", E1.get())
    print("Student Address: ", E2.get())

    id= E.get()
    name = E1.get()
    address = E2.get()


    if selection in ('Insert'):
        con = pymysql.connect(host="localhost", user="root", password="root", database="PYTHONDATA")
        cur = con.cursor()
        
        query = "create table if not exists student (id char(20) Not null,\
            name char(20), address char(20))"
        cur.execute(query)
        con.commit()

        insQuery="insert into student \
            (id,name,address) values ('%s','%s','%s')"%(id,name,address)
        try:
            cur.execute(insQuery)
            con.commit()
            print("Student", id, name, address)
        except Error as e:
            print("Error",e)
            con.rollback()
            print("Table student not created succssfully")
        finally:
            con.close()

        
    elif selection in ('Update'):
        try:
            query = "UPDATE student SET name = %s, address = %s WHERE id = %s"
            con = pymysql.connect(host="localhost", user="root", password="root", database="PYTHONDATA")
            cur = con.cursor()
            cur.execute(query, (name, address, id))
            con.commit()
        except Error as e:
            print("Error", e)
            con.rollback()
        finally:
            con.close()

    elif selection in ('Delete'):
        try:
            query = "DELETE FROM student WHERE id = %s"
            con = pymysql.connect(host="localhost", user="root", password="root", database="PYTHONDATA")
            cur = con.cursor()
            cur.execute(query, (id,))
            con.commit()
        except Error as e:
            print("Error", e)
            con.rollback()
        finally:
            con.close()


    elif selection in ('Select'):
        try:
            query = "SELECT * FROM student WHERE id = %s"
            con = pymysql.connect(host="localhost", user="root", password="root", database="PYTHONDATA")
            cur = con.cursor()
            cur.execute(query, (id,))
            
            # Fetch the result
            result = cur.fetchall()
            
            # Process the result, for example, print it
            for row in result:
                print("Student ID:", row[0])
                print("Student Name:", row[1])
                print("Student Address:", row[2])

            con.commit()

        except Error as e:
            print("Error", e)
            con.rollback()
        finally:
            con.close()







BInsert = tkinter.Button(text="Insert", fg="black",bg='orange',
                         font=('arial',20,'bold'),command=lambda:myButtonEvent('Insert'))
BInsert.grid(row=5, column = 0)

BUpdate = tkinter.Button(text="Update", fg="black",bg='orange',
                         font=('arial',20,'bold'),command=lambda:myButtonEvent('Update'))
BUpdate.grid(row=5, column = 1)

BDelete = tkinter.Button(text="Delete", fg="black",bg='orange',
                         font=('arial',20,'bold'),command=lambda:myButtonEvent('Delete'))
BDelete.grid(row=7, column = 0)

BSelect = tkinter.Button(text="Select", fg="black",bg='orange',
                         font=('arial',20,'bold'),command=lambda:myButtonEvent('Select'))
BSelect.grid(row=7, column = 1)



mainloop()





