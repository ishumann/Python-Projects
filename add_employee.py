from tkinter import *
import tkinter as tk
from backend import Data_management


class Add_employee(tk.Frame):
    """docstring for Add_employee"""
    def __init__(self, add_emp_window):
        self.add_emp_window = add_emp_window
        global db
        db = Data_management()
        global emp_window, emp_name, job_title
        
        emp_window = add_emp_window

        heading=Label(add_emp_window,bg="white",text="Employee Management System",font=("Helvetica 17 bold"))
        heading.grid(row=0,column=0,columnspan=4,padx=15,pady=15)

        name_label = Label(add_emp_window, text="Employee Name : ").grid(row=1, sticky=E, pady=5)
        job_title_label = Label(add_emp_window, text="Job Title : ").grid(row=2, sticky=E)

        emp_name = Entry(add_emp_window)
        emp_name.grid(row=1, column=1, pady=5)
        job_title = Entry(add_emp_window)
        job_title.grid(row=2, column=1)

        savebtn=Button(add_emp_window, text="Save", width=10, background = '#5c4fa1', foreground = "white",command= lambda: save())
        savebtn.grid(row=3, column=0,columnspan=2, pady=10)

        closebtn=Button(add_emp_window, text="Close", width=10, background = '#5c4fa1', foreground = "white",command= lambda: close())
        closebtn.grid(row=3, column=1,columnspan=2, pady=10)


def save():
   name= emp_name.get()
   title= job_title.get()
   db.insertdata(name, title)
   emp_name.delete(0, END)
   job_title.delete(0, END)


def close():
    emp_window.destroy()