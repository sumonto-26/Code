"""import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# setup
root = ttk.Window(themename = "darkly")
root.title("button")
root.geometry("700x400")

# Buttons
def button_func():
    print("a basic button")
    print (radio_var.get())

button_string = tk.StringVar(value = "A button with string var")
# button = ttk.Button(master = root, text = "a simple button", command = button_func)
# button = ttk.Button(master = root, text = "a simple button", command = lambda: print("a basic button"))
button = ttk.Button(master = root, text = "a simple button", command = button_func, textvariable = button_string)
button.pack()





# CHECKBUTTON

# check_var = tk.StringVar()
check_var = tk.StringVar(value = "on")
# check_var = tk.IntVar()
# check_var = tk.BooleanVar()
# check_var = tk.DoubleVar()

# check = ttk.Checkbutton(master = root, text = "checkbox 1")
# check = ttk.Checkbutton(master = root, text = "checkbox 1", command = lambda: print("check button changed"))
'''check = ttk.Checkbutton(
    master = root,
    text = "checkbox 1",
    command = lambda: print(check_var.get()),
    variable = check_var 
    )'''
check1 = ttk.Checkbutton(master = root, text = "checkbox button 1" )
check1.pack()

    
check2 = ttk.Checkbutton(
    master = root,
    text = "checkbox button 2 ",
    command = lambda: print(check_var.get()),
    variable = check_var ,
    onvalue = "on",
    offvalue = "off"
    )

check2.pack()


# RADIO BUTTON
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    master = root,
    text = "Radio button 1",
    value = 2,
    command = lambda: print("radio 1 value == radio 3 value"),
    variable = radio_var )
radio1.pack()

# radio2 = ttk.Radiobutton(master = root, text = "Radio button 2")
'''radio2 = ttk.Radiobutton(
    master = root,
    text = "Radio button 2",
    value = "radio 1",
    command = lambda: print("radio button 2 changed"))'''

radio2 = ttk.Radiobutton(
    master = root,
    text = "Radio button 2",
    value = "Radio button 2",
    variable = radio_var,
    command = lambda: print(radio_var.get()))

radio2.pack()

radio3 = ttk.Radiobutton(
    master = root,
    text = "Radio button 3",
    value = "2", 
    command = lambda: print("radio 1 value == radio 3 value"),
    variable = radio_var )

radio3.pack()



root.mainloop()"""

import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk

# setup
root = tk.Tk()
root.title("button")
root.geometry("700x400")

def radio_func():
    print(check_bool.get())
    check_bool.set(False)

# data
radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

# exersise radios
exersise_radio1 = ttk.Radiobutton(
    master = root,
    text = "Radio A", 
    value = "A",
    command = radio_func,
    variable = radio_string
    )

exersise_radio2 = ttk.Radiobutton(
    master = root,
    text = "Radio B", 
    value = "B",
    command = radio_func,
    variable = radio_string
    )

exersise_check = ttk.Checkbutton(
    master = root,
    text = "exersise check",
    variable = check_bool,
    command = lambda: print(radio_string.get()))

# layout
exersise_radio1.pack()
exersise_radio2.pack()
exersise_check.pack()

# run
root.mainloop()