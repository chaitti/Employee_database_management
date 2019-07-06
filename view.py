
from pymysql import *
from tkinter import *
from tkinter.ttk import *
class view:
    def __init__(self):
        self.root=Tk()
        self.t1=Treeview(self.root,columns=("eid","name","age","post","salary"))
        self.t1.heading("eid", text="Employee_Id")
        self.t1.heading("name",text="Employee_Name")
        self.t1.heading("age",text="Age")
        self.t1.heading("post",text="Post")
        self.t1.heading("salary",text="Salary")
        self.t1["show"]="headings"
        conn=connect("127.0.0.1","root","","employee")
        cr=conn.cursor()
        s="select * from employee_data"
        cr.execute(s)
        result=cr.fetchall()
        i=0
        for row in result:
            self.t1.insert("",index=i,value=row)
            i=i+1
        self.t1.pack()
        self.root.mainloop()
