import tkinter as tk
from window import MainWindow

def main():

    root = tk.Tk()
    
    root.title("Employee Database")
    root.resizable(False,False)
    root.geometry()
    fm = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()