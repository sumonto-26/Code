import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk

def button_func():
    print("button pressed")

# root
root = tk.Tk()
root.title("simple textbox")
root.geometry("900x600")
root.maxsize(1000, 700)

# ttk widgets
label = ttk.Label(master = root, text = "This is a Textbox", font = "none 20 bold")
label.pack()

# Creat widges
tk.Text(master = root) .pack()

# Creat Entry
entry = ttk.Entry(master = root)
entry.pack()

# Exersise Label
exersise_label = ttk.Label(master = root, text = "My Label")
exersise_label.pack()

# Creat Button
button = ttk.Button(master = root, text = "A button", command = button_func)
button.pack() 

# Exersise Button
exersise_Button = ttk.Button(master=root, text="button")
exersise_Button.pack()


root.mainloop()