from tkinter import  *
from tkinter.messagebox import *
from admin_page import *
class admin():
    def enter1(self):
        if self.tf1=="" or self.tf2=="":
            showinfo("","Enter data before submission")
        else:
            username=self.tf1.get()
            password=self.tf2.get()
            f=open("credentials",'r')
            if username =="chaitty_8166" and password =="archisha@123*":
                showinfo("","Welcome")
                admin_page()

            else:
                showinfo("","Wrong Username or password")
                self.tf1.delete(0,END)
                self.tf2.delete(0, END)
    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.lb1=Label(self.root,text="Enter your credentials")
        self.lb1.grid(row=1,column=1)
        self.lb2 = Label(self.root, text="Username")
        self.lb2.grid(row=2, column=0)
        self.lb3 = Label(self.root, text="Password")
        self.lb3.grid(row=3, column=0)
        self.tf1=Entry(self.root,text="")
        self.tf1.grid(row=2,column=1)
        self.tf2 =Entry(self.root, )
        self.tf2.grid(row=3, column=1)
        self.bt1=Button(self.root,text="Enter",command=self.enter1)
        self.bt1.grid(row=4,column=2)
        self.root.mainloop()
