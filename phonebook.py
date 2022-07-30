from tkinter import *
import tkinter.ttk
import tkinter.messagebox as tmsg
import pymysql

root=Tk()

# ************* All variables***********
name_var=StringVar()
number_var=StringVar()
email_var=StringVar()
dob_var=StringVar()
category_var=StringVar()

def add():
    if name_var.get()=="" and number_var.get()=="":
        tmsg.showerror("Attention","Name and number are mandetory fields dont left these fields black")
    else:
        con=pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="pb"
        )
        mycursor=con.cursor()
        sql="INSERT INTO phonebook (name,number,email,dob,category) VALUES (%s,%s,%s,%s,%s)"
        val=(name_var.get(),number_var.get(),email_var.get(),dob_var.get(),category_var.get())
        mycursor.execute(sql,val)
        con.commit()
        display()
        con.close()
        tmsg.showinfo("Attention","Data has been Added successfully")

def display():
    con=pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="pb"
    )
    cursor=con.cursor()
    cursor.execute("select* from phonebook where number=%s",number_var.get())
    rows=cursor.fetchall()
    if(rows!=0):
        table_book.delete(*table_book.get_children())
        for row in rows:
            table_book.insert("",END,value=row)
        con.commit()
    con.close()
def delete():
    if(number_var.get()==""):
        tmsg.showerror("Attention","Please select the field which has to be deleted")
    else:
        con=pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="pb"
        )
        mycursor=con.cursor()
        mycursor.execute("delete  from phonebook where number=%s",number_var.get())
        con.commit()
        clear()
        tmsg.showinfo("Attention","Selected Data has been deleted successfully")
        con.close()

def update():
    if(number_var.get()==""):
        tmsg.showerror("Attention","Please select the feilds which you want to update")
    else:
        con=pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="pb"
        )
        mycursor=con.cursor()
        mycursor.execute("update phonebook set name=%s,email=%s,dob=%s,category=%s where number=%s",(name_var.get(),email_var.get(),dob_var.get(),category_var.get(),number_var.get()))
        con.commit()
        clear()
        con.close()

def search():
    con=pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="pb"
    )
    mycursor=con.cursor()
    if(name_var.get()=="" and number_var.get()=="" and email_var.get()=="" and dob_var.get() and category_var.get()):
        tmsg.showerror("Attention","Please enter field to search")
    else:
        mycursor.execute(f"select * from phonebook where name like '%{name_var.get()}%' and number like '%{number_var.get()}%' and email like '%{email_var.get()}%' and dob like '%{dob_var.get()}%' and category like '%{category_var.get()}%'")
        rows=mycursor.fetchall()
        if(rows!=0):
            table_book.delete(*table_book.get_children())
            for row in rows:
                table_book.insert("",END,values=row)
            con.commit()
        con.close()

def clear():
    name_var.set("")
    number_var.set("")
    email_var.set("")
    dob_var.set("")
    category_var.set("")
    table_book.delete(*table_book.get_children())

def fetchall():
    con=pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="pb"

    )
    mycursor=con.cursor()
    mycursor.execute("select * from phonebook")
    rows=mycursor.fetchall()
    if(rows!=0):
        table_book.delete(*table_book.get_children())
        for row in rows:
            table_book.insert("",END,value=row)
        con.commit()
    con.close()

def getcursor(event):
    global rows
    cursor=table_book.focus()
    row=table_book.item(cursor)
    rows=row['values']
    name_var.set(rows[0])
    number_var.set(rows[1])
    email_var.set(rows[2])
    dob_var.set(rows[3])
    category_var.set(rows[4])


def exit():
    ask=tmsg.askyesno("Attention","If you really want to exit")
    if ask== True:
        root.destroy()
    else:
        pass


root.title("PhoneBook")
root.geometry("1000x600+100+50")
root.config(bg="yellow")
mainframe=Frame(root,bd=10,relief=SUNKEN,bg="orange")
mainframe.place(x=30,y=15,width=950,heigh=550)

headingFrame=Frame(mainframe,bd=5,relief=GROOVE,bg="blue")
headingFrame.place(x=200,y=10,width=500,height=50)

heading=Label(headingFrame,text="Welcome to PhoneBook",bg="blue",font="lucida 20 bold")
heading.grid(row=0,column=0,padx=70,sticky=W)

delFrame=Frame(mainframe,bd=5,relief=GROOVE,bg="red")
delFrame.place(x=20,y=90,width=890,height=400)

nameL=Label(delFrame,text="Name:",font="lucida 20 bold",bg="red")
nameL.grid(row=0,column=0,padx=10,pady=10,sticky=W)
nameE=Entry(delFrame,font="luciad 10 bold",bd=2,relief=SUNKEN,width=20,textvariable=name_var)
nameE.grid(row=0,column=1)

numberL=Label(delFrame,text="Number:",font="lucida 20 bold",bg="red")
numberL.grid(row=1,column=0,padx=10,pady=10,sticky=W)

numberE=Entry(delFrame,font="luciad 10 bold",bd=2,relief=SUNKEN,width=20,textvariable=number_var)
numberE.grid(row=1,column=1)

emailL=Label(delFrame,text="Email:",font="lucida 20 bold",bg="red")
emailL.grid(row=2,column=0,padx=10,pady=10,sticky=W)

emailE=Entry(delFrame,font="luciad 10 bold",bd=2,relief=SUNKEN,width=20,textvariable=email_var)
emailE.grid(row=2,column=1)

dobL=Label(delFrame,text="DOB:",font="lucida 20 bold",bg="red")
dobL.grid(row=3,column=0,padx=10,pady=10,sticky=W)

dobE=Entry(delFrame,font="luciad 10 bold",bd=2,relief=SUNKEN,width=20,textvariable=dob_var)
dobE.grid(row=3,column=1)

categoryL=Label(delFrame,text="Catogery:",font="lucida 20 bold",bg="red")
categoryL.grid(row=4,column=0,padx=10,pady=10,sticky=W)

categoryE=Entry(delFrame,font="luciad 10 bold",bd=2,relief=SUNKEN,width=20,textvariable=category_var)
categoryE.grid(row=4,column=1)

btnFrame=Frame(delFrame,bd=5,relief=GROOVE,bg="pink")
btnFrame.place(x=20,y=320,width=820,height=50)

addbtn=Button(btnFrame,text="ADD",bd=5,relief=RIDGE,font="lucida 10 bold",width=10,bg="orange",command=add)
addbtn.grid(row=0,column=0,padx=10,pady=3)

displaybtn=Button(btnFrame,text="DISPLAY",bd=5,relief=RIDGE,font="lucida 10 bold",width=10,bg="orange",command=fetchall)
displaybtn.grid(row=0,column=1,padx=10,pady=3)

searchbtn=Button(btnFrame,text="SEARCH",bd=5,relief=RIDGE,font="lucida 10 bold",width=10,bg="orange",command=search)
searchbtn.grid(row=0,column=2,padx=10,pady=3)

deletebtn=Button(btnFrame,text="DELETE",bd=5,relief=RIDGE,font="lucida 10 bold",width=10,bg="orange",command=delete)
deletebtn.grid(row=0,column=3,padx=10,pady=3)

clearbtn=Button(btnFrame,text="CLEAR",bd=5,relief=RIDGE,font="lucida 10 bold",width=10,bg="orange",command=clear)
clearbtn.grid(row=0,column=4,padx=10,pady=3)

updatebtn=Button(btnFrame,text="UPDATE",bd=5,relief=RIDGE,font="lucida 10 bold",width=10,bg="orange",command=update)
updatebtn.grid(row=0,column=5,padx=10,pady=3)

exitbtn=Button(btnFrame,text="EXIT",bd=5,relief=RIDGE,font="lucida 10 bold",width=10,bg="orange",command=exit)
exitbtn.grid(row=0,column=6,padx=10,pady=3)

tableFrame=Frame(delFrame,bd=5,relief=RIDGE,bg="lightgreen")
tableFrame.place(x=330,y=15,width=530,height=280)
Scroll_y=Scrollbar(tableFrame,orient=VERTICAL)
Scroll_x=Scrollbar(tableFrame,orient=HORIZONTAL)

table_book=tkinter.ttk.Treeview(tableFrame,column=("Name","Number","Email","DOB","Category"),yscrollcommand=Scroll_y,xscrollcommand=Scroll_x)
Scroll_y.pack(side=RIGHT,fill=Y)
Scroll_x.pack(side=BOTTOM,fill=X)
Scroll_y.config(command=table_book.yview)
Scroll_x.config(command=table_book.xview)

table_book.heading("Name",text="Name")
table_book.heading("Number",text="Number")
table_book.heading("Email",text="Email")
table_book.heading("DOB",text="Date of Birth")
table_book.heading("Category",text="Category")

table_book["show"]="headings"
table_book.column("Name",width=50)
table_book.column("Number",width=50)
table_book.column("Email",width=50)
table_book.column("DOB",width=50)
table_book.column("Category",width=50)
table_book.pack(fill=BOTH,expand=1)
table_book.bind("<ButtonRelease-1>",getcursor)


root.mainloop()