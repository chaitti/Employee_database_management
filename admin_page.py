from tkinter import  *
from tkinter.messagebox import *
from delete import *
from update import *
from view import *
from add import *
class admin_page:
    def fire1(self):
        add()
    def fire2(self):
        delete()
    def fire3(self):
        update()
    def fire4(self):
        view()
    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.lb1=Label(self.root,text="What do you want to do!!!").grid(row=0,column=0)
        self.b1=Button(self.root,text="Insert",command=self.fire1)
        self.b1.grid(row=2,column=1)
        self.b2 = Button(self.root, text="Delete",command=self.fire2)
        self.b2.grid(row=4, column=1)
        self.b3=Button(self.root,text="Update",command=self.fire3)
        self.b3.grid(row=6,column=1)
        self.b4 = Button(self.root, text="View",command=self.fire4)
        self.b4.grid(row=8, column=1)
        self.root.mainloop()



