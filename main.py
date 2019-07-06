from tkinter import *
from admin import *
from user import *
class main:
    def fire1(self):
        admin()
    def fire2(self):
        user()
    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.lb1=Label(self.root,text="Who are You????").grid(row=0,column=2)
        self.b1=Button(self.root,text="Employee",command=self.fire2)
        self.b2=Button(self.root,text="Administrator",command=self.fire1)
        self.b1.grid(row=6,column=2)
        self.b2.grid(row=6, column=4)
        self.root.mainloop()
obj=main()