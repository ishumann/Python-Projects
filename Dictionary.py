from tkinter import messagebox
import os
from tkinter import *
from PIL import ImageTk, Image
from interface import user_interface as ui
import tkinter as tk
def app():
    root = tk.Tk()
    root.geometry("600x400+300+100")
    root.resizable(False,False)
    root.title("Dictionory")
    frame = ui(root)
    frame.place()
    root.mainloop()
if __name__ =='__main__':
    app()
