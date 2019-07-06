from tkinter import *
from pymysql import *
from tkinter.messagebox import *
class add:
    def insert(self):
            conn = connect("127.0.0.1", "root", "", "employee")
            cr = conn.cursor()
            s="insert into employee_data values(NULL,'"+self.tf1.get()+"',"+self.tf2.get()+",'"+self.tf3.get()+"',"+self.tf4.get()+")";
            cr.execute(s)
            showinfo("",s)
            conn.commit()
            conn.close()
    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.lb1=Label(self.root,text="Enter Employee details:").grid(row=0,column=1)
        self.lb2=Label(self.root,text="Name").grid(row=1,column=0)
        self.lb3 = Label(self.root, text="Age").grid(row=2,column=0)
        self.lb4 = Label(self.root, text="Post").grid(row=3,column=0)
        self.lb5 = Label(self.root, text="Salary").grid(row=4,column=0)
        self.tf1=Entry(self.root,text="")
        self.tf2 = Entry(self.root, text="")
        self.tf3 = Entry(self.root, text="")
        self.tf4 = Entry(self.root, text="")
        self.tf1.grid(row=1,column=1)
        self.tf2.grid(row=2, column=1)
        self.tf3.grid(row=3, column=1)
        self.tf4.grid(row=4, column=1)
        self.bt1=Button(self.root,text="Insert",command=self.insert)
        self.bt1.grid(row=5,column=1)
        self.root.mainloop()
