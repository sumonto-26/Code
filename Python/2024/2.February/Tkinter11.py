import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Frames and parenting")
root.geometry("600x400")


frame = tk.Frame(master = root, width = 200, height = 100, borderwidth = 10)
frame.pack()


root.mainloop()