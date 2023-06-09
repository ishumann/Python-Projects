from tkinter import *
from tkinter import messagebox
import tkinter as tk
from add_employee import Add_employee 
from edit_employee import Edit_employee 
from backend import Data_management

class MainWindow(tk.Frame):
    """
    this Class is for the main window when application run

    """
    def __init__(self, root):
        self.root = root
        global rootwindow, db, listbox, lst
        db =Data_management()
        lst = db.viewdata()
        rootwindow = root
        # app heading
        heading=Label(root,bg="white",text="Employee Management System",font=("Helvetica 17 bold"))
        heading.grid(row=0,column=0,columnspan=5,padx=15,pady=15)

        add_btn= Button(root,text= "Add Employee",  background = '#5c4fa1', foreground = "white", command= lambda: create())
        add_btn.grid(row=1, column=0, padx=0, pady=10)


        edit_btn= Button(root,text= "Edit",  background = '#5c4fa1', foreground = "white", command=lambda: edit())
        edit_btn.grid(row=1, column=1, padx=0, pady=10)



        reload_btn= Button(root,text= "Reload", background = '#5c4fa1', foreground = "white",command = lambda: reload())
        reload_btn.grid(row=1, column=2, padx=0, pady=10)


        delete_btn= Button(root,text= "delete",  background = '#5c4fa1', foreground = "white", border= None, command= lambda: delete())
        delete_btn.grid(row=1, column=3, padx=0, pady=10)

        listbox = Listbox(root,selectmode=SINGLE, width=50, height=10, )
        listbox.grid(row=2,column=0,columnspan=4,sticky=W,padx=15,pady=15)
        scrollbar = Scrollbar(root, orient=VERTICAL)

        scrollbar.grid(row=2,column=4,rowspan= 1,sticky=N+S+W, padx=5,pady=5)
        scrollbar.config(command=listbox.yview)
        listbox.insert('end', *lst)

        # Copyright label
        l4 = Label(root, text="Designed and Developed by @IMPRIME")
        l4.grid(row=3, column=0, columnspan=5, pady= 10)



def create():
    add_emp_window = tk.Toplevel(rootwindow)

    add_emp_window.title("Add Employee")
    add_emp_window.resizable(False,False)
    # add_emp_window.geometry("500x300")
    Add_employee(add_emp_window)
    add_emp_window.mainloop()
    lst = db.viewdata()
    listbox.delete(0, tk.END)
    listbox.insert("end", *lst)

        
def reload():
    lst= db.viewdata()
    listbox.delete(0, tk.END)
    listbox.insert('end', *lst)


def edit():
    edit_select = listbox.curselection()
    select_item = listbox.get(edit_select)
    arr = select_item.split(' ')
    if  edit_select == ():
        messagebox.showerror("Error", "Atleast select an item to edit")
    else:
        id = arr[0]
        edit_emp_window = tk.Toplevel(rootwindow)
        Edit_employee(edit_emp_window, id )
        edit_emp_window.title("Edit Employee Details")
        edit_emp_window.resizable(False,False)
        # add_emp_window.geometry("500x300")
        edit_emp_window.mainloop()


def delete():
    edit_select = listbox.curselection()
    select_item = listbox.get(edit_select)
    arr = select_item.split(' ')
    if  edit_select == ():
        messagebox.showerror("Error", "Atleast select an item to delete")
    else:
        id = arr[0]
        db.deletedata(id)
        lst = db.viewdata()
        listbox.delete(0, tk.END)
        listbox.insert("end", *lst)
    