'''import tkinter as tk
from tkinter import ttk

def button_func():
    print(entry.get())
    string_var.set("")

# root 
root = tk.Tk()
root.title("Tkinter Variables")
root.geometry("500x400")

# tkinter variable
string_var = tk.StringVar(value = "start value")

# widgets:
label = ttk.Label(master = root, text = "anything", textvariable = string_var, font = "none 20 bold")
label.pack()

entry = ttk.Entry(master = root, textvariable = string_var)
entry.pack()

button = ttk.Button(master = root, text = "print", command = button_func)
button.pack()


# run
root.mainloop()'''


# Exersise

import tkinter as tk
from tkinter import ttk

# set up
root = tk.Tk()
root.geometry("600x400")
root.title("Exersise")
root.minsize(500, 300)


# tkinter variable
string_var = tk.StringVar(value = "test" ) 

label = ttk.Label(master = root, text = "write anything", font = "none 20 bold", textvariable = string_var )
label.pack()

entry1 = ttk.Entry(master = root, textvariable = string_var)
entry1.pack()

entry2 = ttk.Entry(master = root, textvariable = string_var)
entry2.pack()


# run
root.mainloop()

