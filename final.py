from cProfile import label
from dataclasses import dataclass
from re import L
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from time import strftime
from tokenize import String
from unicodedata import name

from numpy import place

root=Tk()
root.geometry("800x800")
root.title("LIBRARY NAME")
root.configure(bg="#94b7b5")

root.title("VIT Library")

separator = ttk.Separator(root, orient='vertical')    #right partition
separator.place(relx=0.83, rely=0, relwidth=0.2, relheight=1)


separator = ttk.Separator(root, orient='horizontal')   #bottom partition
separator.place(relx=0, rely=0.83, relwidth=1, relheight=1)

import os          #refresh button
root.title("VIT-B Library")
def refresh():
    root.destroy()
    os.popen("final.py") #change refresh.py according to yours program name
button_1 =Button(root,text = "Refresh",command = refresh).place(x=80,y=550)




menubar=Menu(root)
#adding optins to menubar
file=Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New FIle', command=None)
file.add_command(label='Open', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

edit=Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find Again', command=None)

help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

root.config(menu=menubar)

#headiing labels include
a=Label(root,text="****// VIT-B library //****",font=70).place(x=500,y=50)
b=Label(root,text="Add New",font=10).place(x=200,y=150)
c=Label(root,text="Issue Book",font=10).place(x=600,y=150)
d=Label(root,text="Return Book",font=10).place(x=930,y=150)

         #entry widgets
         
#Adding entry
import mysql.connector
database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="prem@2002"
    )
cursor=database.cursor()
cursor.execute("use exibition")
navar=StringVar()
covar=StringVar()
shvar=StringVar()


def submit():
    
    nam=navar.get()
    bookcod=covar.get()
    shelfn=shvar.get()
    
    
    sql="insert into library (book_name,book_code,shelf_number) values(%s,%s,%s)"
    t=(nam,bookcod,shelfn)
    cursor.execute(sql,t)
    database.commit()
    
    
    navar.set("")
    covar.set("")
    shvar.set("")
    
    


namelabel=Label(root,text="Book Name").place(x=100,y=230)
nameentry=Entry(root,textvariable=navar,width=27).place(x=220,y=230)

checkinlabel=Label(root,text="Book code").place(x=100,y=260)
checkinentry=Entry(root,textvariable=covar,width=27).place(x=220,y=260)

checkoutlabel=Label(root,text="Shelf Number").place(x=100,y=290)
checkoutentry=Entry(root,textvariable=shvar,width=27).place(x=220,y=290)

subutton=Button(root, text="Submit", command=submit).place(x=230,y=400)



#issue book
import mysql.connector
_database_=mysql.connector.connect(
    host="localhost",
    user="root",
    password="prem@2002"
    )
_cursor_=_database_.cursor()
_cursor_.execute("use exibition")
regvar=StringVar()
codevar=StringVar()
namevar=StringVar()


def submit():
    
    reg=regvar.get()
    bookcode=codevar.get()
    bname=namevar.get()
    
    
    sql="insert into library_data (reg_no,book_code,book_name) values(%s,%s,%s)"
    t=(reg,bookcode,bname)
    _cursor_.execute(sql,t)
    _database_.commit()
    
    
    regvar.set("")
    codevar.set("")
    namevar.set("")
    
    # Create text widget and specify size.
    T = Text(root, height = 5, width = 52)
    # Create label
        
    Fact = """The book has been issued"""
        
    T.pack(side=BOTTOM)
        
    # Insert The Fact.
    T.insert(END, Fact)
    
    


namelabel=Label(root,text="Reg Num").place(x=500,y=230)
nameentry=Entry(root,textvariable=regvar,width=27).place(x=600,y=230)

checkinlabel=Label(root,text="Book code").place(x=500,y=260)
checkinentry=Entry(root,textvariable=codevar,width=27).place(x=600,y=260)

checkoutlabel=Label(root,text="Book name").place(x=500,y=290)
checkoutentry=Entry(root,textvariable=namevar,width=27).place(x=600,y=290)

sub_button=Button(root,text="Submit",command=submit).place(x=630,y=400)





#Return book
import mysql.connector
db_=mysql.connector.connect(
    host="localhost",
    user="root",
    password="prem@2002"
    )
_cu_=db_.cursor()
_cu_.execute("use exibition")

cvar=StringVar()
rvar=StringVar()
returnvar = StringVar()

def submit():
    
    r=rvar.get()
    ret=returnvar.get()
    c=cvar.get()
    
    
    
    
    
                      
    cmd="update library_data set return_date=%s where reg_no=%s and book_code=%s"
    val=(ret,r,c)
    _cu_.execute(cmd,val)
    db_.commit()
        
        
        # Create text widget and specify size.
    T = Text(root, height = 5, width = 52)
        # Create label
        
    Fact = ("""The book has been returned""")
        
    T.pack(side=BOTTOM)
        
        # Insert The Fact.
    T.insert(END, Fact)
     

            
    cvar.set("")
    rvar.set("")
    returnvar.set("")
    
    
name_label=Label(root,text="Reg Num").place(x=850,y=230)
name_entry=Entry(root,textvariable=rvar,width=27).place(x=950,y=230)

name_label=Label(root,text="Book Code").place(x=850,y=260)
name_entry=Entry(root,textvariable=cvar,width=27).place(x=950,y=260)

check_inlabel=Label(root,text="Return Date").place(x=850,y=290)
check_inentry=Entry(root,textvariable=returnvar,width=27).place(x=950,y=290)

sub_button=Button(root,text="Submit",command=submit).place(x=930,y=400)



#whats trending

ac_label=Label(root,text="[What's Trending]",font=10).place(x=1200,y=150)

def submit():
    
    
    
    
    y=db_.cursor()          #ML
    y.execute("use exibition") 
    y.execute("select book_name from library_data")
    z=y.fetchall()
    from scipy import stats  #max repitationyes
    md=stats.mode(z)
    
    
    
    
    
    # Create text widget and specify size.
    T = Text(root, height = 5, width = 52)
    # Create label
        
    Fact = (md, """is trending""")
        
    T.pack(side=BOTTOM)
        
    # Insert The Fact.
    T.insert(END, Fact)
    
button=Button(root,text="Trending",command=submit).place(x=1210,y=230)

#find
nonac_label=Label(root,text="[ Find Book ]",font=10).place(x=1220,y=340)

import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="prem@2002"
    )
cu=db.cursor()
cu.execute("use exibition")

na_var=StringVar()

def submit():
    name=na_var.get()
    
    
    
    
    sql="select shelf_number from library where book_name=%s"
    t=(name)
    _cu_.execute(sql,t)
    z=_cu_.fetchall()
    for i in z:
        if i==name:
            T = Text(root, height = 5, width = 52)
    
    
    
                           
        
        
        
        
        
        # Create text widget and specify sizeT = Text(root, height = 5, width = 52)
        # Create label
        
            Fact = (z)
        
            T.pack(side=BOTTOM)
        
        # Insert The Fact.
            T.insert(END, Fact)
     

            
    na_var.set("")
    
    
name_label=Label(root,text="Book Name").place(x=1190,y=400)
name_entry=Entry(root,textvariable=na_var,width=27).place(x=1260,y=400)



sub_button=Button(root,text="Find",command=submit).place(x=1270,y=450)



root.mainloop()