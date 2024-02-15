"""import tkinter as tk
from tkinter import ttk

# setup 
root = tk.Tk()
root.title("button, fuction and arguments")
root.geometry("600x400")

def button_func(entry_string):
    print("Button pressed")
    print(f"you type {entry_string.get()}")


# widgets
entry_string = tk.StringVar(value = "test")
entry = ttk.Entry(master = root, textvariable = entry_string)
entry.pack()

button = ttk.Button(master = root, text = "button", command = lambda: button_func(entry_string))
button.pack()



# run
root.mainloop()"""

import tkinter as tk
from tkinter import ttk



### pythontutorial.net/tkinter/tkinter^-event-binding ###



# setup 
root = tk.Tk()
root.title("button, fuction and arguments")
root.geometry("800x600")

# widgets
text = tk.Text(root)
text.pack()

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text = "A button")
button.pack()

def get_pos(event):
    print(f" x : {event.x}  y: {event.y}")

# events
# root.bind("<<Alt-KeyPress-a>>", lambda event : print("an event"))
# root.bind("<Alt-KeyPress-a>", lambda event : print(event))
# button.bind("<Alt-KeyPress-a>", lambda event : print(event))
# root.bind("<Motion>", get_pos)
# text.bind("<Motion>", get_pos)
# root.bind("<KeyPress>", lambda event: print("a button was pressed"))
# root.bind("<KeyPress>", lambda event: print(f"a button was pressed ({event.char})"))
# text.bind("<FocusIn>", lambda event: print("text field was selected"))
# entry.bind("<FocusIn>", lambda event: print("entry field was selected"))
# entry.bind("<FocusOut>", lambda event: print("entry field was unselected"))

# exersise:
entry.bind("<Shift-MouseWheel>", lambda event: print("Mousewheel"))

# run
root.mainloop()


# 1 : 50 : 00
