import tkinter as tk
from tkinter import ttk

def button_func():
    
    # Update the Label
    # label.config(text = entry.get())    # ---
    # label.configure(text = entry.get()) #   | same result
    
    label["text"] = entry.get()           # ---
    # entry["state"] = "disabled"

def button_func2():
    label["text"] = "hello"
    entry["state"] = 'enabled'
    
# root 
root = tk.Tk()
root.title("Getting and setting widgets")
root.geometry("800x500")

# widgets
label = ttk.Label(master = root, text = "hello")
label.pack()

entry = ttk.Entry(master = root)
entry.pack()

button = ttk.Button(master = root, text = "change", command = button_func)
button.pack()

button2 = ttk.Button(master = root, text = "reset", command = button_func2)
button2.pack()


# run
root.mainloop()
